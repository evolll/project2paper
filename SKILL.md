# project2paper — Agent Usage Skill

## How to use project2paper

project2paper is a harness that generates a well-structured technical paper from any codebase. You drive the 5-phase pipeline.

### Quick start in Claude Code

```bash
# 1. Clone the harness
git clone https://github.com/evolll/project2paper.git ~/.claude/plugins/project2paper

# 2. In Claude Code, tell it:
"Read AGENTS.md and run the project2paper pipeline on /path/to/target-project."
```

### Configuration

When you tell the agent to run the pipeline, include your preferences:

```
...run the project2paper pipeline on /path with: length=long, tone=academic, format=latex
```

The agent will write `agent-workspace/project-input/config.json` with these values before starting Phase 1.

### Options

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `length` | short, medium, long | medium | Paper depth |
| `tone` | academic, blog, technical-report, tutorial | academic | Writing style |
| `focus` | architecture, features, performance, full | full | Analysis emphasis |
| `format` | markdown, latex, html | latex | Output format |
| `language` | zh-CN, ja-JP, etc. | en | Output language |

### Pipeline phases

| Phase | Agent | Input | Output |
|-------|-------|-------|--------|
| 1 | project-scanner | Project files | project-map.json |
| 2 | project-analyzer | project-map.json + source | architecture.json |
| 3 | research-extractor | analysis files + source | research-findings.json |
| 4 | paper-writer | all analysis + config | paper.{md/tex/html} |
| 5 | paper-reviewer | paper + source | paper-reviewed.{md/tex/html} |

### Important rules

1. **Never edit `agents/`** — agent prompts are protected
2. **Agent-editable**: `agent-workspace/agent_helpers.py`, `agent-workspace/templates/`
3. **Config file**: `agent-workspace/project-input/config.json` — write this at the start
4. **Intermediate analysis**: `agent-workspace/analysis/`
5. **Final output**: `agent-workspace/output/`
6. The agent writes what's missing. If a helper doesn't exist, add it to `agent_helpers.py`.

### Design constraints

- Pipeline is **phase-sequential**
- Agents run **one at a time**
- Paper-reviewer phase is **mandatory**
- If a phase fails, fix and retry that phase only
