# project2paper — Agent Usage Skill

## How to use

project2paper is a Claude Code plugin with a single slash command:

```
/project2paper
/project2paper /path/to/project
```

All arguments are optional. If omitted, you will be prompted interactively.

## Options

```
/project2paper /path/to/project
/project2paper /path/to/project --format latex --interactive --novelty
```

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `--base` | path | — | Path to a baseline project for comparison. Differences will be listed and you will be asked which parts to treat as paper contributions |
| `--format` | markdown, latex, html | latex | Output format |
| `--interactive` | flag | true | Enable phase-by-phase interaction with user feedback |
| `--novelty` | flag | true | Highlight existing work vs novel contributions in the paper |

## Pipeline

The command executes 6 phases sequentially.

### Phase 0 — Interactive Configuration

Read `agents/project-scanner.md`. If `<path>` or other options are missing, prompt the user interactively:

- `ask_project_path` — if `<path>` is missing, prompt until valid path given
- `ask_paper_type` — choose paper length/category (Technical Report / Journal Paper / Thesis)
- `ask_format` — if `--format` is missing (default: latex)
- **If format is `latex`**: `ask_template_path` — **REQUIRED**. The user MUST provide the path to their own `.tex` template file. Validate the path exists. Retry with `ask_template_retry` until a valid path is given. Store as `user_template_path`.
- `ask_base_path` — if `--base` is missing, optional
- `ask_references` — optional reference paper list

Write `agent-workspace/project-input/config.json` with all gathered settings.

### Phase 1 — project-scanner

Read `agents/project-scanner.md`. Walk the project directory, catalog files, detect language/framework. If `--base` is provided, compare with the base project, list differences, and ask the user which parts to treat as contributions. Write `agent-workspace/analysis/project-map.json`.

### Phase 2 — research-extractor (literature search)

Read `agents/research-extractor.md`. Search for base models, dependencies, existing patterns, and flag potential novelty zones. Write `agent-workspace/analysis/research-findings.json`.

### Phase 3 — project-analyzer (novelty analysis + outline)

Read `agents/project-analyzer.md`. Analyze architecture using Phase 2 context, classify novelty per component, generate analysis outline, enter user review loop if interactive. Write `agent-workspace/analysis/architecture.json` and `agent-workspace/analysis/analysis-outline.md`.

### Phase 4 — paper-writer

Read `agents/paper-writer.md`. Generate the paper in academic style at the specified length/focus/format. For LaTeX output: uses `\input{}` (not `\include{}`) to avoid forced page breaks between chapters; writes per-chapter `.tex` files under `output/chapters/` + a `main.tex` root file. Missing content is marked with `\todo{}` placeholders and `\missingfigure{}` for diagrams. If references were provided, they are cited and a `references.bib` is generated. Write to `agent-workspace/output/main.tex` (LaTeX) or `agent-workspace/output/paper.{md|html}`.

### Phase 5 — paper-reviewer

Read `agents/paper-reviewer.md`. Review and refine the paper, write `agent-workspace/output/paper-reviewed.{md|tex|html}`.

## Interactive mode

When `--interactive` is used (default: true), the agent pauses after each phase to present findings and ask for user feedback before proceeding:
- Phase 0: gather all settings interactively if missing
- Before Phase 1, ask the user about their project's novelty mode (manual input vs AI auto-detect)
- After Phase 1, show project summary and confirm. If `--base` was used, also show the comparison and ask which areas are contributions.
- After Phase 2, show research findings and ask for additional related work
- After Phase 3, present analysis outline for user review and modification (loop until confirmed)
- After Phase 4, show draft and ask for adjustments
- After Phase 5, confirm final output

## Novelty highlighting

When `--novelty` is used (default: true), the paper includes inline markers distinguishing:
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
