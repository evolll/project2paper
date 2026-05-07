"""project2paper CLI entry point.

Usage:
  project2paper                            # interactive wizard
  project2paper /path/to/project
  project2paper -i                         # force interactive wizard
  project2paper /path/to/project --output paper.md --length medium --tone academic
  project2paper /path/to/project --format latex --focus architecture
  project2paper --version
  project2paper --help
"""

import argparse
import json
import sys
import os
from pathlib import Path


LENGTH_CHOICES = ["short", "medium", "long"]
LENGTH_HELP = {
    "short": "500-1000 words, 5 sections — quick overview",
    "medium": "2000-4000 words, 8 sections — balanced (default)",
    "long": "5000-10000 words, 11 sections — deep analysis",
}
TONE_CHOICES = ["academic", "blog", "technical-report", "tutorial"]
TONE_HELP = {
    "academic": "Formal, third-person — for researchers (default)",
    "blog": "Conversational, engaging — for developers",
    "technical-report": "Data-driven, factual — for stakeholders",
    "tutorial": "Step-by-step, pedagogical — for learners",
}
FOCUS_CHOICES = ["architecture", "features", "performance", "full"]
FOCUS_HELP = {
    "architecture": "Emphasize system design, layers, relationships",
    "features": "Emphasize user-facing capabilities and workflows",
    "performance": "Emphasize benchmarks, scalability, bottlenecks",
    "full": "Balanced coverage across all aspects (default)",
}
FORMAT_CHOICES = ["markdown", "latex", "html"]
FORMAT_HELP = {
    "markdown": "Readable markdown (default)",
    "latex": "LaTeX — ready for arXiv or conference submission",
    "html": "HTML page with built-in styling",
}

LANGUAGE_OPTIONS = [
    "en", "zh-CN", "zh-TW", "ja-JP", "ko-KR",
    "es-ES", "fr-FR", "de-DE", "pt-BR", "ru-RU", "tr-TR",
]


def resolve_workspace() -> Path:
    env = os.environ.get("PROJECT2PAPER_AGENT_WORKSPACE")
    if env:
        return Path(env).resolve()
    pkg_dir = Path(__file__).resolve().parent.parent.parent
    candidate = pkg_dir / "agent-workspace"
    if candidate.is_dir():
        return candidate
    return Path.cwd() / "agent-workspace"


def interactive_wizard() -> dict:
    print("=" * 56)
    print("  project2paper — Interactive Setup")
    print("=" * 56)

    project = input("\n  Project path: ").strip()
    project_path = Path(project).expanduser().resolve()
    while not project_path.is_dir():
        print(f"  ✗ Not a directory: {project_path}")
        project = input("  Project path: ").strip()
        project_path = Path(project).expanduser().resolve()

    print("\n  ── Paper Length ──")
    for i, k in enumerate(LENGTH_CHOICES, 1):
        print(f"    {i}) {k:8s} — {LENGTH_HELP[k]}")
    length = _pick(LENGTH_CHOICES, "medium")

    print("\n  ── Writing Tone ──")
    for i, k in enumerate(TONE_CHOICES, 1):
        print(f"    {i}) {k:16s} — {TONE_HELP[k]}")
    tone = _pick(TONE_CHOICES, "academic")

    print("\n  ── Analysis Focus ──")
    for i, k in enumerate(FOCUS_CHOICES, 1):
        print(f"    {i}) {k:12s} — {FOCUS_HELP[k]}")
    focus = _pick(FOCUS_CHOICES, "full")

    print("\n  ── Output Format ──")
    for i, k in enumerate(FORMAT_CHOICES, 1):
        print(f"    {i}) {k:8s} — {FORMAT_HELP[k]}")
    fmt = _pick(FORMAT_CHOICES, "latex")

    print("\n  ── Language ──")
    for i, k in enumerate(LANGUAGE_OPTIONS, 1):
        print(f"    {i:2d}) {k}")
    print(f"    Enter: en")
    lang = input("  Language [en]: ").strip()
    if not lang:
        lang = "en"

    return {
        "project_path": str(project_path),
        "length": length,
        "tone": tone,
        "focus": focus,
        "format": fmt,
        "language": lang if lang != "en" else None,
    }


def _pick(choices: list[str], default: str) -> str:
    val = input(f"  Choice [1/{choices.index(default)+1}]: ").strip()
    if not val:
        return default
    if val.isdigit():
        idx = int(val) - 1
        if 0 <= idx < len(choices):
            return choices[idx]
    if val in choices:
        return val
    print(f"  Invalid, using default: {default}")
    return default


def main():
    parser = argparse.ArgumentParser(
        description="project2paper — Turn any codebase into a well-structured paper.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  project2paper                              # interactive wizard\n"
            "  project2paper /path/to/project\n"
            "  project2paper -i                            # force interactive wizard\n"
            "  project2paper . --length short --tone blog\n"
            "  project2paper .. --format latex --length long --focus architecture\n"
            "  project2paper /path/to/project --language zh-CN\n"
        ),
    )
    parser.add_argument("project", type=str, nargs="?", default=None, help="Path to the project to analyze")
    parser.add_argument("--interactive", "-i", action="store_true", help="Force interactive setup wizard")
    parser.add_argument("--output", "-o", type=str, default=None, help="Output paper path")
    parser.add_argument("--format", "-f", type=str, default=None, choices=FORMAT_CHOICES, help="Output format (default: latex in wizard, markdown in CLI)")
    parser.add_argument("--length", "-L", type=str, default=None, choices=LENGTH_CHOICES, help="Paper length")
    parser.add_argument("--tone", "-T", type=str, default=None, choices=TONE_CHOICES, help="Writing tone")
    parser.add_argument("--focus", "-F", type=str, default=None, choices=FOCUS_CHOICES, help="Analysis focus area")
    parser.add_argument("--language", "-l", type=str, default=None, help="Output language (e.g., zh-CN, ja-JP)")
    parser.add_argument("--version", "-v", action="store_true", help="Print version and exit")

    args = parser.parse_args()

    if args.version:
        from project2paper import __version__ as ver
        print(f"project2paper v{ver}")
        sys.exit(0)

    # ── Interactive wizard ──
    if args.interactive or args.project is None:
        cfg = interactive_wizard()
        project_path = Path(cfg["project_path"])
        paper_length = cfg["length"]
        paper_tone = cfg["tone"]
        paper_focus = cfg["focus"]
        paper_format = cfg["format"]
        paper_language = cfg["language"]
        output_path = None
    else:
        project_path = Path(args.project).resolve()
        if not project_path.is_dir():
            print(f"Error: project path '{project_path}' is not a directory", file=sys.stderr)
            sys.exit(1)
        paper_length = args.length or "medium"
        paper_tone = args.tone or "academic"
        paper_focus = args.focus or "full"
        paper_format = args.format or "markdown"
        paper_language = args.language
        output_path = args.output

    workspace = resolve_workspace()
    print(f"\n  Project:  {project_path}")
    print(f"  Length:   {paper_length}")
    print(f"  Tone:     {paper_tone}")
    print(f"  Focus:    {paper_focus}")
    print(f"  Format:   {paper_format}")
    if paper_language:
        print(f"  Language: {paper_language}")

    if output_path:
        output_path = Path(output_path).resolve()
    else:
        ext = {"markdown": "md", "latex": "tex", "html": "html"}[paper_format]
        output_path = workspace / "output" / f"paper.{ext}"

    workspace.mkdir(parents=True, exist_ok=True)
    (workspace / "project-input").mkdir(parents=True, exist_ok=True)
    (workspace / "analysis").mkdir(parents=True, exist_ok=True)
    (workspace / "output").mkdir(parents=True, exist_ok=True)

    meta = {
        "project_path": str(project_path),
        "project_name": project_path.name,
        "output_format": paper_format,
        "output_path": str(output_path),
        "length": paper_length,
        "tone": paper_tone,
        "focus": paper_focus,
        "language": paper_language,
    }
    (workspace / "project-input" / "config.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False))

    print(f"\n  Output:   {output_path}")
    print("\n  project2paper is ready. The agent will now analyze your project and generate the paper.")
    print("  See SKILL.md for detailed agent instructions.")


if __name__ == "__main__":
    main()
