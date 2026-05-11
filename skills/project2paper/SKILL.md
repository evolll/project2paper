---
name: project2paper
description: Analyze any codebase and generate a publication-quality technical paper
argument-hint: ["[<path>] [--base /path/to/base-project] [--format markdown|latex|html] [--novelty]"]
---

# /project2paper

Analyze a codebase and produce a well-structured technical paper. A 6-phase agent pipeline collects settings, scans the project, discovers base models, analyzes novelty, generates an analysis outline, writes the paper, and reviews it.

## Usage

```
/project2paper
/project2paper /path/to/project
/project2paper /path/to/project --base /path/to/base-project --format latex --novelty
```

## Arguments

All arguments are optional. If omitted, you will be prompted interactively.

| Argument | Default | Description |
|----------|---------|-------------|
| `<path>` | prompted | Path to the project. Asked interactively if omitted |
| `--base` | none | Path to a baseline project for comparison. Differences will be listed and you will be asked which parts to treat as paper contributions |
| `--format` | latex | markdown, latex, html. Asked interactively if omitted |
| `--novelty` | true | Highlight existing work vs novel contributions with inline markers |

## Pipeline

The command executes 6 phases sequentially. Each phase reads its agent prompt, processes the project, and saves output to `agent-workspace/`. The agent drives execution — read the SKILL.md in each phase's agent prompt for detailed instructions.

Tone and depth are determined by the paper type selected in Phase 0.

---

## Phase 0 — Interactive Configuration

**Agent prompt:** `agents/project-scanner.md`

1. Prompt the user interactively using `agent_helpers.get_interactive_prompt()` to gather all settings:
   - `ask_project_path` — if `<path>` is missing
   - `ask_paper_type` — ask the user to choose a paper category that determines length and tone:
     1. **Technical Report**: concise, practical, ~500-1K words
     2. **Journal/Conference Paper**: academic, formal, ~2K-4K words
     3. **Thesis/Dissertation**: comprehensive, in-depth, ~5K-10K words
   - `ask_format` — if `--format` is missing (default: latex)
   - `ask_base_path` — if `--base` is missing (default: none)
2. Resolve `<path>` to an absolute path. If it doesn't exist or isn't a directory, error and STOP.
3. If `--base` is provided, resolve it to an absolute path. If it doesn't exist or isn't a directory, error and STOP.
4. Write `agent-workspace/project-input/config.json` with all gathered settings.

---

## Phase 1 — Project Scan

**Agent prompt:** `agents/project-scanner.md`

1. Read config from `agent-workspace/project-input/config.json`
2. Walk the directory tree, catalog every file (exclude `node_modules/`, `__pycache__/`, `.git/`, `dist/`, `build/`)
3. Detect primary language and framework
4. Identify entry points, test files, config files
5. Count files and lines of code per language
6. If `--base` is provided, scan the base project and compare it with the target project. List differences in structure, new files, modified files, and new dependencies.
7. If `--base` is provided, present the differences as an outline and ask the user which parts should be treated as paper contributions (novelty points).
8. If `--base` is provided, write the comparison results (differences, selected contributions, novelty points) into `project-map.json` under the `base_comparison` key.
9. If `--novelty`: ask user to choose novelty identification mode (manual vs auto)
10. Write `agent-workspace/analysis/project-map.json`

---

## Phase 2 — Literature Search & Base Model Discovery

**Agent prompt:** `agents/research-extractor.md`

1. Read the project map from Phase 1
2. Analyze dependencies, identify base models and existing patterns
3. Flag potential novelty zones for Phase 3 analysis
4. Present findings and ask for additional related work
5. Write `agent-workspace/analysis/research-findings.json`

Cover all areas equally (architecture, features, performance).

---

## Phase 3 — Novelty Analysis & Outline Generation

**Agent prompt:** `agents/project-analyzer.md`

1. Read the project map and research findings
2. Analyze architecture using Phase 2 context (base models, patterns)
3. Classify each component as novel/improved/existing/baseline with rationale
4. Generate `agent-workspace/analysis/architecture.json`
5. Generate analysis outline at `agent-workspace/analysis/analysis-outline.md`
6. Present outline to user, loop for modifications until confirmed

---

## Phase 4 — Paper Writing

**Agent prompt:** `agents/paper-writer.md`

1. Read all analysis files and config
2. Write the paper according to the selected paper type (length and tone). Cover architecture, features, and performance evenly unless `base` comparison highlights specific contribution areas.
3. If `--novelty`: include novelty markers inline
4. Output format specified by `format`
5. Write to `agent-workspace/output/paper.{md|tex|html}`

---

## Phase 5 — Paper Review

**Agent prompt:** `agents/paper-reviewer.md`

1. Read the generated paper and config
2. Verify claims against source code
3. Check length compliance
4. If `--novelty`: validate novelty marker accuracy
5. Fix issues directly
6. Write final version to `agent-workspace/output/paper-reviewed.{md|tex|html}`

---

## After completion

Present the output path to the user. The final paper is at `agent-workspace/output/paper-reviewed.{md|tex|html}`.
