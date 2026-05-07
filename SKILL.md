# project2paper — Agent Usage Skill

## How to use

project2paper is a Claude Code plugin with a single slash command:

```
/project2paper /path/to/project
```

## Options

```
/project2paper /path/to/project --length long --tone academic --focus architecture --format latex --language zh-CN
```

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `--length` | short, medium, long | medium | Paper depth |
| `--tone` | academic, blog, technical-report, tutorial | academic | Writing style |
| `--focus` | architecture, features, performance, full | full | Analysis emphasis |
| `--format` | markdown, latex, html | latex | Output format |
| `--language` | zh-CN, ja-JP, etc. | en | Output language |

## Pipeline

| Phase | Agent | Output |
|-------|-------|--------|
| 1 | project-scanner | analysis/project-map.json |
| 2 | project-analyzer | analysis/architecture.json |
| 3 | research-extractor | analysis/research-findings.json |
| 4 | paper-writer | output/paper.{md/tex/html} |
| 5 | paper-reviewer | output/paper-reviewed.{md/tex/html} |

## Rules

- Do not edit `skills/` or `agents/`
- Editable: `agent-workspace/agent_helpers.py`, `agent-workspace/templates/`
- Write config.json to `agent-workspace/project-input/` before Phase 1
- Phases are sequential; if a phase fails, fix and retry only that phase
