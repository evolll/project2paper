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
/project2paper /path/to/your-project --length long --tone academic --focus architecture --format latex --language zh-CN
```

## Pipeline phases

| Phase | Agent | Output |
|-------|-------|--------|
| 1. project-scanner | `agents/project-scanner.md` | `analysis/project-map.json` |
| 2. project-analyzer | `agents/project-analyzer.md` | `analysis/architecture.json` |
| 3. research-extractor | `agents/research-extractor.md` | `analysis/research-findings.json` |
| 4. paper-writer | `agents/paper-writer.md` | `output/paper.tex` |
| 5. paper-reviewer | `agents/paper-reviewer.md` | `output/paper-reviewed.tex` |

## Key files

- `skills/project2paper/SKILL.md` — The `/project2paper` command definition
- `agents/` — Agent prompts for each pipeline phase
- `agent-workspace/` — Config, analysis, output, templates

## Rules

- Never edit `skills/` or `agents/` — those are the harness
- Agent-editable: `agent-workspace/`
- Phases run sequentially; if one fails, fix and retry that phase only
