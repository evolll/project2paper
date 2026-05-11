---
name: project2paper
description: Analyze any codebase and generate a publication-quality technical paper. 5-phase pipeline: project-scanner → research-extractor → project-analyzer → paper-writer → paper-reviewer
license: MIT
compatibility: opencode
metadata:
  audience: developers
  output: latex
---

# project2paper

Turn any codebase into a well-structured technical paper.

## Usage

Tell me the project path and your preferences, and I'll run the 5-phase pipeline:

```
project2paper /path/to/project --base /path/to/base-project --length long --format latex --interactive --novelty
```

## Configuration options

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `--length` | short, medium, long | medium | Paper depth |
| `--base` | path | — | Path to a baseline project for comparison. Differences will be listed and you will be asked which parts to treat as paper contributions |
| `--format` | markdown, latex, html | latex | Output format |
| `--interactive` | flag | false | Enable phase-by-phase user interaction for feedback and verification |
| `--novelty` | flag | false | Highlight existing work vs novel contributions with inline markers |

## Pipeline

Before starting Phase 1, write `agent-workspace/project-input/config.json` with the user's settings.

### Phase 1 — project-scanner

Read `agents/project-scanner.md`. Walk the project directory, catalog files, detect language/framework, write `agent-workspace/analysis/project-map.json`.

### Phase 2 — research-extractor (literature search)

Read `agents/research-extractor.md`. Search for base models, dependencies, existing patterns, and flag potential novelty zones. Write `agent-workspace/analysis/research-findings.json`.

### Phase 3 — project-analyzer (novelty analysis + outline)

Read `agents/project-analyzer.md`. Analyze architecture using Phase 2 context, classify novelty per component, generate analysis outline, enter user review loop if interactive. Write `agent-workspace/analysis/architecture.json` and `agent-workspace/analysis/analysis-outline.md`.

### Phase 4 — paper-writer

Read `agents/paper-writer.md`. Generate the paper in academic style at the specified length/format. If `--base` is provided, emphasize the selected contribution areas, write `agent-workspace/output/paper.{md|tex|html}`.

### Phase 5 — paper-reviewer

Read `agents/paper-reviewer.md`. Review and refine the paper, write `agent-workspace/output/paper-reviewed.{md|tex|html}`.

## Interactive mode

When `--interactive` is used:
- Before Phase 1, ask the user about their project's novelty mode (manual input vs AI auto-detect)
- After Phase 1, show project summary and confirm
- After Phase 2, show research findings and ask for additional related work
- After Phase 3, present analysis outline for user review and modification (loop until confirmed)
- After Phase 4, show draft and ask for adjustments
- After Phase 5, confirm final output

## Novelty highlighting

When `--novelty` is used, each component, feature, and design decision is classified and marked as:
- 🆕 Novel Contribution — new approach/algorithm/design
- ✨ Improved — adapted/optimized from prior work
- 📚 Existing — prior work or dependency
- 🔧 Baseline — common practice

A legend and summary table are included in the output.

## Output

The final paper is at `agent-workspace/output/paper-reviewed.{md|tex|html}`. Present the path to the user.
