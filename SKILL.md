# project2paper — Agent Usage Skill

## How to use

project2paper is a Claude Code plugin with a single slash command:

```
/project2paper /path/to/project
```

## Options

```
/project2paper /path/to/project --length long --focus architecture --format latex --interactive --novelty
```

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `--length` | short, medium, long | medium | Paper depth |
| `--focus` | architecture, features, performance, full | full | Analysis emphasis |
| `--format` | markdown, latex, html | latex | Output format |
| `--interactive` | flag | false | Enable phase-by-phase interaction with user feedback |
| `--novelty` | flag | false | Highlight existing work vs novel contributions in the paper |

## Pipeline

Before starting Phase 1, write `agent-workspace/project-input/config.json` with the user's settings.

### Phase 1 — project-scanner

Read `agents/project-scanner.md`. Walk the project directory, catalog files, detect language/framework, write `agent-workspace/analysis/project-map.json`.

### Phase 2 — research-extractor (literature search)

Read `agents/research-extractor.md`. Search for base models, dependencies, existing patterns, and flag potential novelty zones. Write `agent-workspace/analysis/research-findings.json`.

### Phase 3 — project-analyzer (novelty analysis + outline)

Read `agents/project-analyzer.md`. Analyze architecture using Phase 2 context, classify novelty per component, generate analysis outline, enter user review loop if interactive. Write `agent-workspace/analysis/architecture.json` and `agent-workspace/analysis/analysis-outline.md`.

### Phase 4 — paper-writer

Read `agents/paper-writer.md`. Generate the paper in academic style at the specified length/focus/format, write `agent-workspace/output/paper.{md|tex|html}`.

### Phase 5 — paper-reviewer

Read `agents/paper-reviewer.md`. Review and refine the paper, write `agent-workspace/output/paper-reviewed.{md|tex|html}`.

## Interactive mode

When `--interactive` is used, the agent pauses after each phase to present findings and ask for user feedback before proceeding:
- Before Phase 1, ask the user about their project's novelty mode (manual input vs AI auto-detect)
- After Phase 1, show project summary and confirm
- After Phase 2, show research findings and ask for additional related work
- After Phase 3, present analysis outline for user review and modification (loop until confirmed)
- After Phase 4, show draft and ask for adjustments
- After Phase 5, confirm final output

## Novelty highlighting

When `--novelty` is used, the paper includes inline markers distinguishing:
- 🆕 **Novel Contribution** — Truly new approach/algorithm/design
- ✨ **Improved** — Adapted or optimized from prior work
- 📚 **Existing** — Prior work or dependency
- 🔧 **Baseline** — Common / standard practice

A novelty legend and a summary breakdown appear in the paper.

## Rules

- Do not edit `skills/` or `agents/` unless modifying the plugin itself
- Editable: `agent-workspace/agent_helpers.py`, `agent-workspace/templates/`
- Write config.json to `agent-workspace/project-input/` before Phase 1
- Phases are sequential; if a phase fails, fix and retry only that phase

## Output

The final paper is at `agent-workspace/output/paper-reviewed.{md|tex|html}`. Present the path to the user.
