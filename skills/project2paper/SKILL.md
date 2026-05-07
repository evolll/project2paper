---
name: project2paper
description: Analyze any codebase and generate a publication-quality technical paper
argument-hint: ["<path> [--length short|medium|long] [--tone academic|blog|technical-report|tutorial] [--focus architecture|features|performance|full] [--format markdown|latex|html] [--language en|zh-CN|ja-JP|...]"]
---

# /project2paper

Analyze a codebase and produce a well-structured technical paper. A 5-phase agent pipeline scans the project, analyzes architecture, extracts insights, writes the paper, and reviews it.

## Usage

```
/project2paper /path/to/project
/project2paper /path/to/project --length long --tone academic --focus architecture --format latex
/project2paper /path/to/project --length short --tone blog --language zh-CN
```

## Arguments

| Argument | Default | Description |
|----------|---------|-------------|
| `<path>` | — | Path to the project (required) |
| `--length` | medium | short (500-1K words), medium (2K-4K), long (5K-10K) |
| `--tone` | academic | academic, blog, technical-report, tutorial |
| `--focus` | full | architecture, features, performance, full |
| `--format` | latex | markdown, latex, html |
| `--language` | en | Output language (zh-CN, ja-JP, ko-KR, etc.) |

## Pipeline

The command executes 5 phases sequentially. Each phase reads its agent prompt, processes the project, and saves output to `agent-workspace/`. The agent drives execution — read the SKILL.md in each phase's agent prompt for detailed instructions.

---

## Phase 1 — Project Scan

**Agent prompt:** `agents/project-scanner.md`

1. Read the project path from `$ARGUMENTS`
2. Resolve it to an absolute path. If it doesn't exist or isn't a directory, error and STOP.
3. Walk the directory tree, catalog every file (exclude `node_modules/`, `__pycache__/`, `.git/`, `dist/`, `build/`)
4. Detect primary language and framework
5. Identify entry points, test files, config files
6. Count files and lines of code per language
7. Write `agent-workspace/analysis/project-map.json`

**Before starting Phase 1: write `agent-workspace/project-input/config.json`** with the user's settings (extract `--length`, `--tone`, `--focus`, `--format`, `--language` from arguments; use defaults for missing ones).

---

## Phase 2 — Architecture Analysis

**Agent prompt:** `agents/project-analyzer.md`

1. Read the project map from Phase 1
2. Read key source files (entry points, core modules, configs)
3. Identify architectural pattern, layers, components, relationships
4. Map features, design patterns, data model, API surface
5. Document technology stack
6. Write `agent-workspace/analysis/architecture.json`

Prioritize depth based on the `focus` setting from config.

---

## Phase 3 — Research Extraction

**Agent prompt:** `agents/research-extractor.md`

1. Read the architecture analysis and key source files
2. Identify novel contributions, key decisions, trade-offs
3. Extract lessons learned, pain points, quantifiable metrics
4. Identify target audience
5. Write `agent-workspace/analysis/research-findings.json`

Prioritize based on `focus` setting.

---

## Phase 4 — Paper Writing

**Agent prompt:** `agents/paper-writer.md`

1. Read all analysis files and config
2. Write the paper at the depth specified by `length`, in the tone specified by `tone`, emphasizing the `focus` area
3. Output format specified by `format`, language specified by `language`
4. Write to `agent-workspace/output/paper.{md|tex|html}`

---

## Phase 5 — Paper Review

**Agent prompt:** `agents/paper-reviewer.md`

1. Read the generated paper and config
2. Verify claims against source code
3. Check length/tone/focus compliance
4. Fix issues directly
5. Write final version to `agent-workspace/output/paper-reviewed.{md|tex|html}`

---

## After completion

Present the output path to the user. The final paper is at `agent-workspace/output/paper-reviewed.{md|tex|html}`.
