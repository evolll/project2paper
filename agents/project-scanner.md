---
name: project-scanner
description: Scan a project directory and produce a structured map of files, languages, frameworks, and entry points.
---

# Agent: project-scanner (Phase 0 & 1)

## Role
You handle Phase 0 (interactive configuration) and Phase 1 (project scan).

## Phase 0 — Interactive Configuration

### Input
- `$ARGUMENTS` passed to the `/project2paper` command

### Output
Write to `agent-workspace/project-input/config.json`:
```json
{
  "project_path": "<absolute path>",
  "base_path": "<absolute path or null>",
  "length": "short|medium|long",
  "output_format": "markdown|latex|html",
  "interactive": true,
  "novelty_highlight": true,
  "novelty_mode": "auto"
}
```

### Instructions

Parse `$ARGUMENTS` for `<path>`, `--base`, `--format`, `--interactive`, and `--novelty`.

**Hard rule: if `<path>` is missing, empty, or unresolvable, you MUST prompt interactively. Do NOT silently skip or guess.**

0. **Guard check** — If `$ARGUMENTS` is empty, contains only whitespace, or lacks a resolvable `<path>`: immediately enter full interactive mode. Ask for `project_path`, `paper_type`, `format`, and `base_path` in sequence. Do NOT proceed until `project_path` is provided and validated.

1. **Project path** — If `<path>` is missing, prompt the user with `agent_helpers.get_interactive_prompt("ask_project_path")`. Repeat until a valid path is provided.
2. **Paper type** — If `--length` is missing, prompt the user with `agent_helpers.get_interactive_prompt("ask_paper_type")`. Map the choice to `length`:
   - `1` → `short`
   - `2` → `medium`
   - `3` → `long`
   Default to `medium` if the user skips.
3. **Output format** — If `--format` is missing, prompt the user with `agent_helpers.get_interactive_prompt("ask_format")`. Default to `latex` if the user skips.
4. **Base project** — If `--base` is missing, prompt the user with `agent_helpers.get_interactive_prompt("ask_base_path")`. If the user declines, set `base_path` to `null`.
5. **Interactive mode** — If `--interactive` is missing, default to `true`.
6. **Novelty highlight** — If `--novelty` is missing, default to `true`.
7. Resolve `<path>` to an absolute path. If it doesn't exist or isn't a directory, error and STOP.
8. If `--base` is provided, resolve it to an absolute path. If it doesn't exist or isn't a directory, error and STOP.
9. Write `agent-workspace/project-input/config.json` with all gathered settings.

---

## Phase 1 — Project Scan

### Input
- `agent-workspace/project-input/config.json`

### Output
Write to `agent-workspace/analysis/project-map.json`:
```json
{
  "project_name": "...",
  "language": "...",
  "framework": "...",
  "total_files": 123,
  "total_lines": 45678,
  "languages": { "Python": 60, "TypeScript": 30, ... },
  "dependencies": ["dep1", "dep2", ...],
  "novelty_hints": { "user_provided_novelty": "...", "user_provided_existing": "..." },
  "base_comparison": null
}
```

If `base_path` is present, `base_comparison` will contain:
```json
{
  "base_project_name": "...",
  "summary": "brief description of differences",
  "new_files": ["src/new_feature.py", ...],
  "modified_files": ["src/core.py", ...],
  "removed_files": ["old_module.py", ...],
  "new_dependencies": ["dep3", ...],
  "removed_dependencies": ["dep1", ...],
  "new_features_areas": ["Area A", "Area B"],
  "user_selected_contributions": ["Area A"]
}
```

### Instructions

1. Read `config.json` to get the project path and check `interactive`, `novelty_highlight`, and `base_path` options.
2. Walk the directory tree (exclude node_modules, __pycache__, .git, dist, build, .venv).
3. For each file: record path, extension, line count.
4. Detect the primary language and framework.
5. Identify entry points, test files, config files.
6. Count total files and lines of code per language.

### Base project comparison (config.base_path is set)

If a `base_path` is provided in config.json:

7. **Scan the base project** using the same exclusions and rules as the target project.
8. **Compare the two projects** and generate a difference outline covering:
    - New files/directories (present in target, absent in base)
    - Modified files (same path but different content/size)
    - Removed files/directories (present in base, absent in target)
    - Added dependencies (in target but not in base)
    - Removed dependencies (in base but not in target)
    - New feature areas inferred from file groupings (e.g., "Authentication module", "Payment gateway", "Custom caching layer")
9. **Present the difference outline** to the user as an interactive prompt. Use `agent_helpers.get_interactive_prompt("base_comparison_review", comparison=...)` or a custom prompt.
10. **Ask the user to select contributions**: "Which of the following areas should be treated as paper contributions (novelty points)?" Present a numbered list of the detected new feature areas. Allow the user to select one or more by number, or type `all`.
11. **Store the user's selection** in `base_comparison.user_selected_contributions`.
12. **Store the comparison** in the output JSON under `base_comparison`.

If `interactive` is false, automatically select all detected new feature areas as contributions and store them.

### Interactive mode (config.interactive == true && config.novelty_highlight == true && config.base_path is null)

13. **Ask user to choose novelty identification mode** — Present `ask_novelty_mode` prompt (use `agent_helpers.get_interactive_prompt("ask_novelty_mode")`). Ask the user to choose between **manual** (user describes novelty points) or **auto** (AI discovers novelty). Store the choice in config as `novelty_mode` and update `config.json`.

14. **If manual mode:** — Present `ask_novelty_hints_manual` prompt. Store user's answers in `novelty_hints` in the output JSON: `{ "user_provided_novelty": "...", "user_provided_existing": "..." }`.

15. **If auto mode:** — Present `ask_novelty_hints_auto` prompt (informational only). Set `novelty_hints` to `null` in the output JSON.

16. **After scanning** — Present the summary and ask if user wants to proceed to Phase 2.

Be thorough but fast. Focus on structure, not content.
