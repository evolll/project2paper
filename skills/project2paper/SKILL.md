---
name: project2paper
description: Analyze any codebase and generate a publication-quality technical paper
argument-hint: ["<path> [--base /path/to/base-project] [--length short|medium|long] [--format markdown|latex|html] [--interactive] [--novelty]"]
---

# /project2paper

Analyze a codebase and produce a well-structured technical paper. A 5-phase agent pipeline scans the project, discovers base models, analyzes novelty, generates an analysis outline, writes the paper, and reviews it.

## Usage

```
/project2paper /path/to/project
/project2paper /path/to/project --base /path/to/base-project --length long --format latex --interactive --novelty
```

## Arguments

| Argument | Default | Description |
|----------|---------|-------------|
| `<path>` | — | Path to the project (required) |
| `--base` | — | Path to a baseline project for comparison. Differences will be listed and you will be asked which parts to treat as paper contributions |
| `--length` | medium | short (500-1K words), medium (2K-4K), long (5K-10K) |
| `--format` | latex | markdown, latex, html |
| `--interactive` | true | Enable phase-by-phase user interaction for feedback and verification |
| `--novelty` | true | Highlight existing work vs novel contributions with inline markers |

## Pipeline

The command executes 5 phases sequentially. Each phase reads its agent prompt, processes the project, and saves output to `agent-workspace/`. The agent drives execution — read the SKILL.md in each phase's agent prompt for detailed instructions.

The paper is written in academic style (formal, third-person) by default.

---

## Phase 1 — Project Scan

**Agent prompt:** `agents/project-scanner.md`

1. Read the project path from `$ARGUMENTS`
2. Resolve it to an absolute path. If it doesn't exist or isn't a directory, error and STOP.
3. If `--base` is provided, resolve it to an absolute path. If it doesn't exist or isn't a directory, error and STOP.
4. Walk the directory tree, catalog every file (exclude `node_modules/`, `__pycache__/`, `.git/`, `dist/`, `build/`)
5. Detect primary language and framework
6. Identify entry points, test files, config files
7. Count files and lines of code per language
8. If `--base` is provided, scan the base project and compare it with the target project. List differences in structure, new files, modified files, and new dependencies. Present the differences as an outline and ask the user which parts should be treated as paper contributions (novelty points).
9. If `--interactive` and `--novelty`: ask user to choose novelty identification mode (manual vs auto)
10. Write `agent-workspace/analysis/project-map.json`

**Before starting Phase 1: write `agent-workspace/project-input/config.json`** with the user's settings (extract `--length`, `--base`, `--format`, `--interactive`, `--novelty` from arguments; use defaults for missing ones). Store `base_path` if `--base` is provided.

---

## Phase 2 — Literature Search & Base Model Discovery

**Agent prompt:** `agents/research-extractor.md`

1. Read the project map from Phase 1
2. Analyze dependencies, identify base models and existing patterns
3. Flag potential novelty zones for Phase 3 analysis
4. If `--interactive`: present findings and ask for additional related work
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
6. If `--interactive`: present outline to user, loop for modifications until confirmed

---

## Phase 4 — Paper Writing

**Agent prompt:** `agents/paper-writer.md`

1. Read all analysis files and config
2. Write the paper at the depth specified by `length`, in academic tone. Cover architecture, features, and performance evenly unless `base` comparison highlights specific contribution areas.
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
