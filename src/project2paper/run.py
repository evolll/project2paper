"""project2paper CLI entry point.

Usage:
  project2paper /path/to/project
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
TONE_CHOICES = ["academic", "blog", "technical-report", "tutorial"]
FOCUS_CHOICES = ["architecture", "features", "performance", "full"]
FORMAT_CHOICES = ["markdown", "latex", "html"]


def resolve_workspace() -> Path:
    env = os.environ.get("PROJECT2PAPER_AGENT_WORKSPACE")
    if env:
        return Path(env).resolve()
    pkg_dir = Path(__file__).resolve().parent.parent.parent
    candidate = pkg_dir / "agent-workspace"
    if candidate.is_dir():
        return candidate
    return Path.cwd() / "agent-workspace"


def main():
    parser = argparse.ArgumentParser(
        description="project2paper — Turn any codebase into a well-structured paper.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  project2paper /path/to/project\n"
            "  project2paper . --length short --tone blog\n"
            "  project2paper ../my-project --format latex --length long --focus architecture\n"
            "  project2paper /path/to/project --tutorial --language zh-CN\n"
        ),
    )
    parser.add_argument("project", type=str, help="Path to the project to analyze")
    parser.add_argument("--output", "-o", type=str, default=None, help="Output paper path")
    parser.add_argument("--format", "-f", type=str, default="markdown", choices=FORMAT_CHOICES, help="Output format (default: markdown)")
    parser.add_argument("--length", "-L", type=str, default="medium", choices=LENGTH_CHOICES, help="Paper length: short (500-1K words), medium (2-4K words), long (5-10K words)")
    parser.add_argument("--tone", "-T", type=str, default="academic", choices=TONE_CHOICES, help="Writing tone: academic, blog, technical-report, tutorial")
    parser.add_argument("--focus", "-F", type=str, default="full", choices=FOCUS_CHOICES, help="Analysis focus area")
    parser.add_argument("--language", "-l", type=str, default=None, help="Output language (e.g., zh-CN, ja-JP)")
    parser.add_argument("--version", "-v", action="store_true", help="Print version and exit")

    args = parser.parse_args()

    if args.version:
        from project2paper import __version__ as ver
        print(f"project2paper v{ver}")
        sys.exit(0)

    project_path = Path(args.project).resolve()
    if not project_path.is_dir():
        print(f"Error: project path '{project_path}' is not a directory", file=sys.stderr)
        sys.exit(1)

    workspace = resolve_workspace()
    print(f"Project:  {project_path}")
    print(f"Workspace: {workspace}")
    print(f"Format:   {args.format}")
    print(f"Length:   {args.length}")
    print(f"Tone:     {args.tone}")
    print(f"Focus:    {args.focus}")
    if args.language:
        print(f"Language: {args.language}")

    if args.output:
        output_path = Path(args.output).resolve()
    else:
        ext = {"markdown": "md", "latex": "tex", "html": "html"}[args.format]
        output_path = workspace / "output" / f"paper.{ext}"

    workspace.mkdir(parents=True, exist_ok=True)
    (workspace / "project-input").mkdir(parents=True, exist_ok=True)
    (workspace / "analysis").mkdir(parents=True, exist_ok=True)
    (workspace / "output").mkdir(parents=True, exist_ok=True)

    meta = {
        "project_path": str(project_path),
        "project_name": project_path.name,
        "output_format": args.format,
        "output_path": str(output_path),
        "length": args.length,
        "tone": args.tone,
        "focus": args.focus,
        "language": args.language,
    }
    (workspace / "project-input" / "config.json").write_text(json.dumps(meta, indent=2))

    print(f"\nOutput:   {output_path}")
    print("\nproject2paper is ready. The agent will now analyze your project and generate the paper.")
    print("See SKILL.md for detailed agent instructions.")
    print("\nTip: Paste the following into your agent:")
    print(f"  Read SKILL.md and AGENTS.md, then run the project2paper pipeline on {project_path}")


if __name__ == "__main__":
    main()
