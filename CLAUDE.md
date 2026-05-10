# project2paper

Turn any codebase into a well-structured technical paper. Claude Code plugin — use `/project2paper`.

## Quick start

```bash
# Clone the plugin
git clone https://github.com/evolll/project2paper.git ~/.claude/plugins/project2paper
```

Then in Claude Code, run:

```
/project2paper /path/to/your-project
```

With options:

```
/project2paper /path/to/your-project --base /path/to/base-project --length long --format latex --interactive --novelty
```

New features:
- `--interactive` — Phase-by-phase user interaction (review findings, provide hints, verify classifications)
- `--novelty` — Distinguish existing work from novel contributions with inline markers and a summary table
- Default tone is academic, output language is English

## Pipeline phases (revised order)

| Phase | Agent | Output |
|-------|-------|--------|
| 1. project-scanner | `agents/project-scanner.md` | `analysis/project-map.json` |
| 2. research-extractor (literature search) | `agents/research-extractor.md` | `analysis/research-findings.json` |
| 3. project-analyzer (novelty analysis + outline) | `agents/project-analyzer.md` | `analysis/architecture.json` + `analysis/analysis-outline.md` |
| 4. paper-writer | `agents/paper-writer.md` | `output/paper.tex` |
| 5. paper-reviewer | `agents/paper-reviewer.md` | `output/paper-reviewed.tex` |

## Key files

- `skills/project2paper/SKILL.md` — The `/project2paper` command definition
- `agents/` — Agent prompts for each pipeline phase
- `agent-workspace/` — Config, analysis, output, templates
- `agent-workspace/analysis/analysis-outline.md` — Analysis outline (generated in Phase 3 for user review)

## Rules

- Never edit `skills/` or `agents/` during normal usage — those are the harness
- Agent-editable: `agent-workspace/`
- Phases run sequentially; if one fails, fix and retry that phase only
- For interactive mode, use `agent-workspace/agent_helpers.py` → `get_interactive_prompt()` to present checkpoints
- For novelty highlighting, use `agent-workspace/agent_helpers.py` → `render_novelty_marker()` to format badges
- Phase 3 includes a user review loop for the analysis outline
