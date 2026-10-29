"""Write a disk-backed text-file inventory and a compact context-sizing summary.

No source bodies are emitted. Python standard library only; Git is optional.
"""

import argparse
import json
import os
from pathlib import Path
import subprocess


EXCLUDED_DIRS = {
    ".git", ".hg", ".svn", "node_modules", "__pycache__", ".venv", "venv",
    "dist", "build", "vendor", "coverage", ".next", ".nuxt", ".cache",
    ".ua", ".understand-anything",
}
GENERATED_WORKSPACE_DIRS = {"analysis", "output", "project-input"}


def excluded_directory(parts, excluded):
    return (any(part in excluded for part in parts)
            or any(parent == "agent-workspace" and child in GENERATED_WORKSPACE_DIRS
                   for parent, child in zip(parts, parts[1:])))


def candidate_paths(root, excluded):
    """Honor Git ignores where available, otherwise walk with directory pruning."""
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-z", "--cached", "--others",
             "--exclude-standard"], capture_output=True, check=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        def walk_error(error):
            raise error  # An incomplete directory walk must not look complete.

        for directory, dirs, files in os.walk(root, onerror=walk_error, followlinks=False):
            relative = Path(directory).relative_to(root)
            dirs[:] = sorted(d for d in dirs
                             if not excluded_directory((*relative.parts, d), excluded))
            for name in sorted(files):
                yield Path(directory, name).relative_to(root)
    else:
        # Cached/other entries can overlap; Git outputs paths relative to root.
        for raw in sorted(set(result.stdout.split(b"\0")) - {b""}):
            path = Path(os.fsdecode(raw))
            if not excluded_directory(path.parts[:-1], excluded):
                yield path


def text_stats(path):
    """Stream bytes locally, skipping NUL-bearing binary files."""
    size = lines = 0
    last_byte = b""
    with path.open("rb") as source:
        while chunk := source.read(65536):
            if b"\0" in chunk:
                return None
            size += len(chunk)
            lines += chunk.count(b"\n")
            last_byte = chunk[-1:]
    return size, lines + int(bool(size) and last_byte != b"\n")


def scan_project(project_path, output_dir, *, file_threshold=1000,
                 line_threshold=100000, token_threshold=1000000, exclude=()):
    root = Path(project_path).expanduser().resolve()
    output = Path(output_dir).expanduser().resolve()
    if not root.is_dir():
        raise ValueError(f"Project is not a directory: {root}")
    if min(file_threshold, line_threshold, token_threshold) < 1:
        raise ValueError("Thresholds must be positive")
    if output == root or root.is_relative_to(output):
        raise ValueError("Output directory must not contain the project root")
    output.mkdir(parents=True, exist_ok=True)
    summary = {
        "project_path": str(root), "total_files": 0, "total_lines": 0,
        "text_bytes": 0, "estimated_tokens": 0, "by_extension": {},
        "binary_files": 0, "excluded_symlinks": 0, "unreadable_files": 0,
        "excluded_directories": sorted(EXCLUDED_DIRS | set(exclude)),
        "excluded_workspace_paths": [f"agent-workspace/{name}"
                                     for name in sorted(GENERATED_WORKSPACE_DIRS)],
        "thresholds": {"files": file_threshold, "lines": line_threshold,
                       "estimated_tokens": token_threshold},
        "inventory_path": str(output / "file-inventory.jsonl"),
    }
    with (output / "file-inventory.jsonl").open("w", encoding="utf-8") as inventory:
        for relative in candidate_paths(root, EXCLUDED_DIRS | set(exclude)):
            path = root / relative
            if path.is_symlink() or any(p.is_symlink() for p in path.parents if p != root):
                summary["excluded_symlinks"] += 1
                continue
            if path.is_relative_to(output):
                continue
            try:
                stats = text_stats(path)
            except OSError:
                summary["unreadable_files"] += 1
                continue
            if stats is None:
                summary["binary_files"] += 1
                continue
            size, lines = stats
            extension = path.suffix.lower() or "[no extension]"
            group = summary["by_extension"].setdefault(extension, {"files": 0, "lines": 0})
            group["files"] += 1
            group["lines"] += lines
            summary["total_files"] += 1
            summary["total_lines"] += lines
            summary["text_bytes"] += size
            inventory.write(json.dumps({"path": relative.as_posix(), "extension": extension,
                                        "bytes": size, "lines": lines}, ensure_ascii=True) + "\n")
    summary["estimated_tokens"] = (summary["text_bytes"] + 3) // 4
    reasons = [name for name, value, threshold in (
        ("files", summary["total_files"], file_threshold),
        ("lines", summary["total_lines"], line_threshold),
        ("estimated_tokens", summary["estimated_tokens"], token_threshold),
    ) if value >= threshold]
    summary["scan_strategy"] = "knowledge_graph" if reasons else "direct"
    summary["thresholds_exceeded"] = reasons
    (output / "scan-summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=True) + "\n", encoding="utf-8",
    )
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_path")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--file-threshold", type=int, default=1000)
    parser.add_argument("--line-threshold", type=int, default=100000)
    parser.add_argument("--token-threshold", type=int, default=1000000)
    parser.add_argument("--exclude", action="append", default=[], metavar="DIRECTORY_NAME")
    args = parser.parse_args()
    try:
        summary = scan_project(
            args.project_path, args.output_dir, file_threshold=args.file_threshold,
            line_threshold=args.line_threshold, token_threshold=args.token_threshold,
            exclude=args.exclude,
        )
    except (ValueError, OSError) as error:
        parser.error(str(error))
    print(json.dumps({"summary_path": str(Path(args.output_dir).expanduser().resolve()
                                           / "scan-summary.json"),
                      "scan_strategy": summary["scan_strategy"]}))


if __name__ == "__main__":
    main()
