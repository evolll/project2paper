# project2paper — Agent Guide

project2paper is a thin harness that connects coding agents to any project, enabling them to analyze it and generate a well-structured technical paper.

## Code priorities
- **Clarity** — The paper should be readable and well-structured
- **Accuracy** — Every claim must be verifiable from the source code
- **Depth** — Go beyond surface-level; analyze trade-offs, patterns, decisions

## Overview

### Agent prompts (read these for each phase)
- `agents/project-scanner.md` — Phase 1: scan and map the project
- `agents/project-analyzer.md` — Phase 2: deep architecture analysis
- `agents/research-extractor.md` — Phase 3: focus-aware insight extraction
- `agents/paper-writer.md` — Phase 4: write paper (uses length/tone/focus from config)
- `agents/paper-reviewer.md` — Phase 5: review and refine

### Agent-editable files
- `agent-workspace/agent_helpers.py` — Custom analysis or paper-generation helpers
- `agent-workspace/templates/` — Output format templates with length variants

### Config file (write this first)
- `agent-workspace/project-input/config.json` — Write with user's length/tone/focus/format/language choices before starting Phase 1

### Session artifact files
- `agent-workspace/analysis/project-map.json` — Project structure map
- `agent-workspace/analysis/architecture.json` — Architecture analysis
- `agent-workspace/analysis/research-findings.json` — Research insights
- `agent-workspace/output/paper.md` — Generated paper

## Instructions for agents

1. Read this file first
2. Read SKILL.md for usage instructions
3. Ask the user for their preferences, or read them from the instructions
4. Write `agent-workspace/project-input/config.json` with length/tone/focus/format/language
5. Read the agent prompt for the current pipeline phase
6. Execute the phase — adjust depth based on `length`, tone based on `tone`, emphasis based on `focus`
7. Save outputs to the correct paths
8. Proceed to the next phase

Remember: you drive the pipeline. The harness provides structure; the intelligence is yours.
