# project2paper — Agent Guide

project2paper is a Codex / Claude Code plugin and OpenCode skill that generates a technical paper from a codebase via six sequential phases (0–5).

## When the user runs `$project2paper` (Codex) or `/project2paper` (Claude Code)

1. Read `skills/project2paper/SKILL.md` — it defines the full flow
2. Parse arguments: project path, `--base`, `--format`, `--interactive`, `--novelty`. The LaTeX template is asked interactively if format is latex.
3. Follow the skill's runtime/path rules: bundled prompts/helpers/templates are under the plugin root; generated `agent-workspace/` is under the writable run root. Execute Phase 0 to gather settings and write config.json (`interactive` and `novelty_highlight` default to true).
4. Execute Phase 1–5 by reading each agent prompt in sequence. Phase 1 performs a size preflight before reading source. For large targets or baselines, use an available graph tool such as Understand Anything, or a bounded local module index; downstream phases retrieve modules on demand and verify claims against source.
5. In interactive mode, use `agent-workspace/agent_helpers.py` helper functions for user prompts and novelty rendering

## Code priorities
- **Clarity** — The paper should be readable and well-structured
- **Accuracy** — Every claim must be verifiable from the source code
- **Depth** — Go beyond surface-level; analyze trade-offs, patterns, decisions

## File structure

| Path | Purpose |
|------|---------|
| `skills/project2paper/SKILL.md` | `/project2paper` command — reads this first |
| `.codex-plugin/plugin.json` | Codex plugin manifest; uses the shared skill |
| `.agents/plugins/marketplace.json` | Codex marketplace registration |
| `skills/project2paper/references/large-projects.md` | Graph-assisted scanning, fallback, and context handoff |
| `agent-workspace/scan_inventory.py` | Size preflight; inventory on disk, compact summary |
| `agents/project-scanner.md` | Phase 1: scan project structure |
| `agents/research-extractor.md` | Phase 2: literature search & base model discovery |
| `agents/project-analyzer.md` | Phase 3: novelty analysis, outline generation, user review loop |
| `agents/paper-writer.md` | Phase 4: paper writing |
| `agents/paper-reviewer.md` | Phase 5: review and refine |
| `agent-workspace/project-input/config.json` | User settings written by Phase 1 pre-flight |
| `agent-workspace/analysis/` | Intermediate analysis artifacts (project-map.json ← Phase 1, research-findings.json ← Phase 2, architecture.json + analysis-outline.md ← Phase 3) |
| `agent-workspace/output/` | Final paper output |
| `agent-workspace/templates/` | Output format templates (examples). Users can provide their own .tex template during interactive setup |

## Instructions

1. Read `skills/project2paper/SKILL.md` first — follow its flow
2. Parse user arguments, write config.json
3. For each phase, read the corresponding agent prompt and execute
4. Use academic tone by default. Adjust depth based on `length`. If `--base` is provided, emphasize the selected contribution areas
5. Save outputs to the correct paths
6. Present the final output path to the user
