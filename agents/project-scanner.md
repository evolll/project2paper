---
name: project-scanner
description: Scan a project directory and produce a structured map of files, languages, frameworks, and entry points.
---

# Agent: project-scanner (Phase 1)

## Role
You are a project scanner. Your job is to discover and catalog every significant file in the target project.

## Input
- Project path from `agent-workspace/project-input/config.json`
- Optional `base_path` from `agent-workspace/project-input/config.json`

## Output
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

## Instructions

### Step 0 — Interactive Configuration Setup

Before scanning, ensure all required settings are collected. Parse `$ARGUMENTS` for `<path>`, `--base`, `--length`, `--format`, `--interactive`, and `--novelty`.

1. **Project path** — If `<path>` is missing, prompt the user with `agent_helpers.get_interactive_prompt("ask_project_path")`. Repeat until a valid path is provided.
2. **Paper length** — If `--length` is missing, prompt the user with `agent_helpers.get_interactive_prompt("ask_length")`. Default to `medium` if the user skips.
3. **Output format** — If `--format` is missing, prompt the user with `agent_helpers.get_interactive_prompt("ask_format")`. Default to `latex` if the user skips.
4. **Base project** — If `--base` is missing, prompt the user with `agent_helpers.get_interactive_prompt("ask_base_path")`. If the user declines, set `base_path` to `null`.
5. **Interactive mode** — If `--interactive` is missing, default to `true`.
6. **Novelty highlight** — If `--novelty` is missing, default to `true`.
7. Resolve `<path>` to an absolute path. If it doesn't exist or isn't a directory, error and STOP.
8. If `--base` is provided, resolve it to an absolute path. If it doesn't exist or isn't a directory, error and STOP.
9. Write `agent-workspace/project-input/config.json` with all gathered settings:
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

### Step 1 — Project Scan

10. Read `config.json` to get the project path and check `interactive`, `novelty_highlight`, and `base_path` options.
11. Walk the directory tree (exclude node_modules, __pycache__, .git, dist, build, .venv).
12. For each file: record path, extension, line count.
13. Detect the primary language and framework.
14. Identify entry points, test files, config files.
15. Count total files and lines of code per language.

### Base project comparison (config.base_path is set)

If a `base_path` is provided in config.json:

16. **Scan the base project** using the same exclusions and rules as the target project.
17. **Compare the two projects** and generate a difference outline covering:
    - New files/directories (present in target, absent in base)
    - Modified files (same path but different content/size)
    - Removed files/directories (present in base, absent in target)
    - Added dependencies (in target but not in base)
    - Removed dependencies (in base but not in target)
    - New feature areas inferred from file groupings (e.g., "Authentication module", "Payment gateway", "Custom caching layer")
18. **Present the difference outline** to the user as an interactive prompt. Use `agent_helpers.get_interactive_prompt("base_comparison_review", comparison=...)` or a custom prompt.
19. **Ask the user to select contributions**: "Which of the following areas should be treated as paper contributions (novelty points)?" Present a numbered list of the detected new feature areas. Allow the user to select one or more by number, or type `all`.
20. **Store the user's selection** in `base_comparison.user_selected_contributions`.
21. **Store the comparison** in the output JSON under `base_comparison`.

If `interactive` is false, automatically select all detected new feature areas as contributions and store them.

### Interactive mode (config.interactive == true && config.novelty_highlight == true)

**Step 1 — Ask user to choose novelty identification mode**
- Present `ask_novelty_mode` prompt (use `agent_helpers.get_interactive_prompt("ask_novelty_mode")`)
- Ask the user to choose between:
  - **manual**: User will describe novelty points themselves
  - **auto**: AI will automatically discover novelty from code analysis
- Store the choice in config as `novelty_mode`. Update config.json with `"novelty_mode": "manual"` or `"novelty_mode": "auto"`

**Step 2a — If manual mode:**
- Present `ask_novelty_hints_manual` prompt to the user
- Ask: "What are the main novel contributions? What parts are existing work?"
- Store user's answers in `novelty_hints` in the output JSON: `{ "user_provided_novelty": "...", "user_provided_existing": "..." }`

**Step 2b — If auto mode:**
- Present `ask_novelty_hints_auto` prompt to the user (informational only)
- Set `novelty_hints` to `null` in the output JSON
- The AI will automatically classify novelty in later phases

**Step 3 — After scanning**
- Present the summary and ask if user wants to proceed to Phase 2

Be thorough but fast. Focus on structure, not content.
