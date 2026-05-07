---
name: project2paper
description: Analyze any codebase and generate a publication-quality technical paper. 5-phase pipeline: project-scanner → project-analyzer → research-extractor → paper-writer → paper-reviewer
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
project2paper /path/to/project --length long --tone academic --focus architecture --format latex
```

## Configuration options

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `--length` | short, medium, long | medium | Paper depth |
| `--tone` | academic, blog, technical-report, tutorial | academic | Writing style |
| `--focus` | architecture, features, performance, full | full | Analysis emphasis |
| `--format` | markdown, latex, html | latex | Output format |
| `--language` | zh-CN, ja-JP, etc. | en | Output language |

## Pipeline

Before starting Phase 1, write `agent-workspace/project-input/config.json` with the user's settings.

### Phase 1 — project-scanner

Read `agents/project-scanner.md`. Walk the project directory, catalog files, detect language/framework, write `agent-workspace/analysis/project-map.json`.

### Phase 2 — project-analyzer

Read `agents/project-analyzer.md`. Analyze architecture, identify layers/components/patterns, write `agent-workspace/analysis/architecture.json`.

### Phase 3 — research-extractor

Read `agents/research-extractor.md`. Extract novel insights, key decisions, lessons learned, write `agent-workspace/analysis/research-findings.json`.

### Phase 4 — paper-writer

Read `agents/paper-writer.md`. Generate the paper at the specified length/tone/focus/format/language, write `agent-workspace/output/paper.{md|tex|html}`.

### Phase 5 — paper-reviewer

Read `agents/paper-reviewer.md`. Review and refine the paper, write `agent-workspace/output/paper-reviewed.{md|tex|html}`.

## Output

The final paper is at `agent-workspace/output/paper-reviewed.{md|tex|html}`. Present the path to the user.
