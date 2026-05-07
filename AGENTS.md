# project2paper — Agent Guide

project2paper is a thin harness that connects coding agents to any project, enabling them to analyze it and generate a well-structured technical paper.

## Code priorities
- **Clarity** — The paper should be readable and well-structured
- **Accuracy** — Every claim must be verifiable from the source code
- **Depth** — Go beyond surface-level description; analyze trade-offs, patterns, and decisions

## Overview

### Core code (protected — do not edit)
- `src/project2paper/run.py` — CLI entry point
- `src/project2paper/pipeline.py` — Pipeline phase definitions
- `src/project2paper/helpers.py` — Auto-imported utility functions
- `src/project2paper/templates.py` — Paper section structure templates

### Agent prompts (read these for each phase)
- `agents/project-scanner.md` — Phase 1: scan and map the project
- `agents/project-analyzer.md` — Phase 2: deep architecture analysis
- `agents/research-extractor.md` — Phase 3: extract novel insights
- `agents/paper-writer.md` — Phase 4: write the paper
- `agents/paper-reviewer.md` — Phase 5: review and refine

### Agent-editable files
- `agent-workspace/agent_helpers.py` — Custom analysis or paper-generation helpers
- `agent-workspace/templates/` — Output format templates

### Session artifact files
- `agent-workspace/project-input/config.json` — Project config and metadata
- `agent-workspace/analysis/project-map.json` — Project structure map
- `agent-workspace/analysis/architecture.json` — Architecture analysis
- `agent-workspace/analysis/research-findings.json` — Research insights
- `agent-workspace/output/paper.md` — Generated paper

## Instructions for agents

1. Read this file first to understand the architecture
2. Read SKILL.md for day-to-day usage instructions
3. Read install.md for setup instructions
4. Then read the agent prompt for the current pipeline phase
5. Execute the phase and save outputs to the correct paths
6. Proceed to the next phase

Remember: you (the agent) are the one doing the analysis and writing. The harness provides structure, but the intelligence is yours. Don't be afraid to add depth — a good paper is worth the effort.
