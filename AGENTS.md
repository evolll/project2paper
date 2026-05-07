# project2paper — Agent Guide

project2paper is a Claude Code plugin that generates a technical paper from any codebase via a 5-phase pipeline.

## When the user runs `/project2paper`

1. Read `skills/project2paper/SKILL.md` — it defines the full flow
2. Parse arguments: project path, `--length`, `--tone`, `--focus`, `--format`, `--language`
3. Write `agent-workspace/project-input/config.json` with parsed settings
4. Execute Phase 1–5 by reading each agent prompt in sequence

## Code priorities
- **Clarity** — The paper should be readable and well-structured
- **Accuracy** — Every claim must be verifiable from the source code
- **Depth** — Go beyond surface-level; analyze trade-offs, patterns, decisions

## File structure

| Path | Purpose |
|------|---------|
| `skills/project2paper/SKILL.md` | `/project2paper` command — reads this first |
| `agents/project-scanner.md` | Phase 1: scan project structure |
| `agents/project-analyzer.md` | Phase 2: architecture analysis |
| `agents/research-extractor.md` | Phase 3: insight extraction |
| `agents/paper-writer.md` | Phase 4: paper writing |
| `agents/paper-reviewer.md` | Phase 5: review and refine |
| `agent-workspace/project-input/config.json` | User settings written by Phase 1 pre-flight |
| `agent-workspace/analysis/` | Intermediate analysis artifacts |
| `agent-workspace/output/` | Final paper output |
| `agent-workspace/templates/` | Output format templates |

## Instructions

1. Read `skills/project2paper/SKILL.md` first — follow its flow
2. Parse user arguments, write config.json
3. For each phase, read the corresponding agent prompt and execute
4. Adjust depth based on `length`, tone based on `tone`, emphasis based on `focus`
5. Save outputs to the correct paths
6. Present the final output path to the user
