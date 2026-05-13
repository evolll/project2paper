---
name: project2paper
description: Analyze any codebase and generate a publication-quality technical paper. 6-phase pipeline: project-scanner → research-extractor → project-analyzer → paper-writer → paper-reviewer
license: MIT
compatibility: opencode
metadata:
  audience: developers
  output: latex
---

# project2paper

Turn any codebase into a well-structured technical paper.

## Usage

All arguments are optional. If omitted, you will be prompted interactively.

```
project2paper
project2paper /path/to/project --base /path/to/base-project --format latex --interactive --novelty
```

## Configuration options

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `--base` | path | — | Path to a baseline project for comparison. Differences will be listed and you will be asked which parts to treat as paper contributions |
| `--format` | markdown, latex, html | latex | Output format |
| `--interactive` | flag | true | Enable phase-by-phase user interaction for feedback and verification |
| `--novelty` | flag | true | Highlight existing work vs novel contributions with inline markers |

## Pipeline

The command executes 6 phases sequentially.

### Phase 0 — Interactive Configuration

Read `agents/project-scanner.md`. If `<path>` or other options are missing, prompt the user interactively:

- `ask_project_path` — if `<path>` is missing, prompt until valid path given
- `ask_paper_type` — choose paper length/category
- `ask_format` — if `--format` is missing (default: latex)
- **If format is `latex`**: `ask_template_path` — **REQUIRED**. The user MUST provide the path to their own `.tex` template file. Validate the path exists. Retry with `ask_template_retry` until valid. Store as `user_template_path`.
- `ask_base_path` — if `--base` is missing, optional
- `ask_references` — optional reference paper list

Write `agent-workspace/project-input/config.json` with all gathered settings.

### Phase 1 — project-scanner

Read `agents/project-scanner.md`. Walk the project directory, catalog files, detect language/framework, write `agent-workspace/analysis/project-map.json`.

### Phase 2 — research-extractor (literature search)

Read `agents/research-extractor.md`. Search for base models, dependencies, existing patterns, and flag potential novelty zones. Write `agent-workspace/analysis/research-findings.json`.

### Phase 3 — project-analyzer (novelty analysis + outline)

Read `agents/project-analyzer.md`. Analyze architecture using Phase 2 context, classify novelty per component, generate analysis outline, enter user review loop if interactive. Write `agent-workspace/analysis/architecture.json` and `agent-workspace/analysis/analysis-outline.md`.

### Phase 4 — paper-writer

Read `agents/paper-writer.md`. Generate the paper in academic style at the specified length/format. For LaTeX, writes per-chapter `.tex` files under `output/chapters/` + `main.tex`. Missing content uses `\todo{}` and `\missingfigure{}` placeholders. References are cited and a `references.bib` is generated. Write to `agent-workspace/output/main.tex` (LaTeX) or `agent-workspace/output/paper.{md|html}`.

### Phase 5 — paper-reviewer

Read `agents/paper-reviewer.md`. Review and refine the paper, write `agent-workspace/output/paper-reviewed.{md|tex|html}`.

## Interactive mode

When `--interactive` is used (default: true):
- Phase 0: gather all settings interactively if missing
- Before Phase 1, ask the user about their project's novelty mode (manual input vs AI auto-detect)
- After Phase 1, show project summary and confirm
- After Phase 2, show research findings and ask for additional related work
- After Phase 3, present analysis outline for user review and modification (loop until confirmed)
- After Phase 4, show draft and ask for adjustments
- After Phase 5, confirm final output

## Novelty highlighting

When `--novelty` is used (default: true), each component, feature, and design decision is classified and marked as:
- 🆕 Novel Contribution — new approach/algorithm/design
- ✨ Improved — adapted/optimized from prior work
- 📚 Existing — prior work or dependency
- 🔧 Baseline — common practice

A legend and summary table are included in the output.

## Output

The final paper is at `agent-workspace/output/paper-reviewed.{md|tex|html}`. Present the path to the user.
