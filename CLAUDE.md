# project2paper

Turn any codebase into a well-structured technical paper. A self-healing 5-phase pipeline for LLM-powered project documentation.

## Quick start in Claude Code

```bash
# 1. Install the plugin (one-time)
git clone https://github.com/evolll/project2paper.git ~/.claude/plugins/project2paper
pip install -e ~/.claude/plugins/project2paper

# 2. Configure — pick length, tone, format, language
project2paper /path/to/target-project --length long --tone academic --format latex

# 3. Tell Claude Code:
#    "Read AGENTS.md and run the project2paper pipeline."
```

## Pipeline phases

| Phase | File | Output |
|-------|------|--------|
| 1. project-scanner | `agents/project-scanner.md` | `analysis/project-map.json` |
| 2. project-analyzer | `agents/project-analyzer.md` | `analysis/architecture.json` |
| 3. research-extractor | `agents/research-extractor.md` | `analysis/research-findings.json` |
| 4. paper-writer | `agents/paper-writer.md` | `output/paper.tex` |
| 5. paper-reviewer | `agents/paper-reviewer.md` | `output/paper-reviewed.tex` |

## Key files

- `SKILL.md` — Day-to-day usage instructions
- `AGENTS.md` — Agent architecture guide
- `src/project2paper/` — Core Python package (protected, do not edit)
- `agents/` — Agent prompts for each pipeline phase
- `agent-workspace/` — Editable workspace (analysis, output, templates)
- `agent-workspace/agent_helpers.py` — Agent-editable custom helpers

## CLI options

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--length` / `-L` | short, medium, long | medium | Paper depth |
| `--tone` / `-T` | academic, blog, technical-report, tutorial | academic | Writing style |
| `--focus` / `-F` | architecture, features, performance, full | full | Analysis focus |
| `--format` / `-f` | markdown, latex, html | latex | Output format |
| `--language` / `-l` | zh-CN, ja-JP, etc. | — | Output language |

## Rules

- Never edit files inside `src/project2paper/` — core package is protected
- Agent-editable files are in `agent-workspace/`
- Pipeline is phase-sequential; if a phase fails, fix and retry that phase only
