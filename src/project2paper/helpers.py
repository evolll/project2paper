"""Utility helpers for project2paper.

These primitives are auto-imported into the agent workspace context.
"""

import json
import os
from pathlib import Path
from typing import Any


def resolve_workspace() -> Path:
    env = os.environ.get("PROJECT2PAPER_AGENT_WORKSPACE")
    if env:
        return Path(env).resolve()
    pkg_dir = Path(__file__).resolve().parent.parent.parent
    candidate = pkg_dir / "agent-workspace"
    if candidate.is_dir():
        return candidate
    return Path.cwd() / "agent-workspace"


def resolve_project_root() -> Path | None:
    ws = resolve_workspace()
    config_path = ws / "project-input" / "config.json"
    if not config_path.exists():
        return None
    data = json.loads(config_path.read_text())
    return Path(data["project_path"]).resolve()


def get_config() -> dict[str, Any]:
    ws = resolve_workspace()
    config_path = ws / "project-input" / "config.json"
    if not config_path.exists():
        return {}
    return json.loads(config_path.read_text())


def read_output_format() -> str:
    return get_config().get("output_format", "markdown")


def read_language() -> str | None:
    return get_config().get("language")


def save_json(path: str | Path, data: Any) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    return path


def load_json(path: str | Path) -> Any:
    path = Path(path)
    if not path.exists():
        return None
    return json.loads(path.read_text())


def is_binary_file(path: Path) -> bool:
    try:
        with open(path, "rb") as f:
            chunk = f.read(8192)
            return b"\0" in chunk
    except OSError:
        return True


def count_lines(path: Path) -> int:
    try:
        with open(path, "r", errors="replace") as f:
            return sum(1 for _ in f)
    except OSError:
        return 0


def safe_read(path: Path, max_bytes: int = 1024 * 64) -> str:
    try:
        if path.stat().st_size > max_bytes:
            return f"<file too large: {path.stat().st_size} bytes>"
        return path.read_text(errors="replace")
    except OSError as e:
        return f"<error reading: {e}>"
