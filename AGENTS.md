# project2paper — Agent Guide

project2paper is a Claude Code plugin that generates a technical paper from any codebase via a 5-phase pipeline.

## When the user runs `/project2paper`

1. Read `skills/project2paper/SKILL.md` — it defines the full flow
2. Parse arguments: project path, `--length`, `--focus`, `--format`, `--interactive`, `--novelty`
3. Write `agent-workspace/project-input/config.json` with parsed settings (set `interactive: true` if `--interactive` flag, `novelty_highlight: true` if `--novelty` flag)
4. Execute Phase 1–5 by reading each agent prompt in sequence
5. In interactive mode, use `agent-workspace/agent_helpers.py` helper functions for user prompts and novelty rendering

## Code priorities
- **Clarity** — The paper should be readable and well-structured
- **Accuracy** — Every claim must be verifiable from the source code
- **Depth** — Go beyond surface-level; analyze trade-offs, patterns, decisions

## File structure

| Path | Purpose |
|------|---------|
| `skills/project2paper/SKILL.md` | `/project2paper` command — reads this first |
| `agents/project-scanner.md` | Phase 1: scan project structure |
| `agents/research-extractor.md` | Phase 2: literature search & base model discovery |
| `agents/project-analyzer.md` | Phase 3: novelty analysis, outline generation, user review loop |
| `agents/paper-writer.md` | Phase 4: paper writing |
| `agents/paper-reviewer.md` | Phase 5: review and refine |
| `agent-workspace/project-input/config.json` | User settings written by Phase 1 pre-flight |
| `agent-workspace/analysis/` | Intermediate analysis artifacts (project-map.json ← Phase 1, research-findings.json ← Phase 2, architecture.json + analysis-outline.md ← Phase 3) |
| `agent-workspace/output/` | Final paper output |
| `agent-workspace/templates/` | Output format templates |

## Instructions

1. Read `skills/project2paper/SKILL.md` first — follow its flow
2. Parse user arguments, write config.json
3. For each phase, read the corresponding agent prompt and execute
4. Use academic tone by default. Adjust depth based on `length`, emphasis based on `focus`
5. Save outputs to the correct paths
6. Present the final output path to the user
