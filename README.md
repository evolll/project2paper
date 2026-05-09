# project2paper

**Turn any codebase into a well-structured technical paper.**

A 5-phase agent pipeline that analyzes any project and produces a publication-quality paper. Works with **Claude Code** (slash command) and **OpenCode** (skill).

```
/project2paper /path/to/project --length long --format latex --interactive --novelty

  ● Phase 1: project-scanner   → project structure mapped
  ● Phase 2: project-analyzer  → architecture analyzed
  ● Phase 3: research-extractor → insights extracted
  ● Phase 4: paper-writer      → paper drafted
  ● Phase 5: paper-reviewer    → paper reviewed and refined
  │
  ✓ agent-workspace/output/paper.tex — done
```

---

## Quick Start

### Claude Code

```bash
# 1. Add the marketplace (one-time)
claude plugins marketplace add https://github.com/evolll/project2paper

# 2. Install the plugin
claude plugins install project2paper

# 3. Run in Claude Code
/project2paper /path/to/your-project

# 4. With options
/project2paper /path/to/your-project --length long --format latex --interactive --novelty
```

### OpenCode

```bash
# 1. Clone to global skills (one-time)
git clone https://github.com/evolll/project2paper.git ~/.config/opencode/skills/project2paper

# 2. In OpenCode, tell the agent:
run the project2paper pipeline on /path/to/project with --length long --format latex --interactive --novelty
```

Auto-discovered via `.opencode/skills/project2paper/SKILL.md`.

---

## Options

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `--length` | short, medium, long | medium | short (500-1K words), medium (2K-4K), long (5K-10K) |
| `--focus` | architecture, features, performance, full | full | What to emphasize |
| `--format` | markdown, latex, html | latex | Output format |
| `--interactive` | flag | false | Phase-by-phase user interaction for feedback and verification |
| `--novelty` | flag | false | Highlight existing work vs novel contributions with inline markers |

### Length

| Length | Words | Sections | Best for |
|--------|-------|----------|----------|
| short | 500-1K | 5 | Executive summary, quick overview |
| medium | 2K-4K | 8 | Standard documentation |
| long | 5K-10K | 11 | Publication, deep analysis |

### Style

The paper is written in **academic** style (formal, third-person, problem-to-solution flow) by default.

---

## How it works

```
/project2paper /my-project --length long --interactive --novelty

  ┌─ Phase 1 ──────────────────────────────────┐
  │  agent/project-scanner.md                  │
  │  → walks directory, catalogs files         │
  │  → detects language, framework, deps       │
  │  → [interactive] asks novelty mode+ hints  │
  │  → writes project-map.json                 │
  └────────────────────────────────────────────┘
                     ↓
  ┌─ Phase 2 ──────────────────────────────────┐
  │  agent/research-extractor.md               │
  │  → searches for base models & dependencies │
  │  → identifies existing patterns & patterns │
  │  → flags potential novelty zones           │
  │  → writes research-findings.json           │
  └────────────────────────────────────────────┘
                     ↓
  ┌─ Phase 3 ──────────────────────────────────┐
  │  agent/project-analyzer.md                 │
  │  → analyzes architecture using Phase 2 ctx │
  │  → classifies each component: novel/existing│
  │  → generates analysis-outline.md           │
  │  → [interactive] user reviews outline loop │
  │  → writes architecture.json + outline      │
  └────────────────────────────────────────────┘
                     ↓
  ┌─ Phase 4 ──────────────────────────────────┐
  │  agent/paper-writer.md                     │
  │  → uses length/tone/focus/novelty/outline  │
  │  → generates paper with novelty markers    │
  │  → writes output/paper.{md|tex|html}       │
  └────────────────────────────────────────────┘
                     ↓
  ┌─ Phase 5 ──────────────────────────────────┐
  │  agent/paper-reviewer.md                   │
  │  → verifies claims against source          │
  │  → checks length/tone/focus/novelty        │
  │  → validates novelty markers accuracy      │
  │  → writes output/paper-reviewed.{ext}      │
  └────────────────────────────────────────────┘
```

---

## Project Structure

```
project2paper/
├── .claude-plugin/plugin.json          # Claude Code plugin registration
├── .opencode/skills/project2paper/     # OpenCode skill
│   └── SKILL.md
├── skills/
│   └── project2paper/SKILL.md          # /project2paper command (Claude)
├── agents/
│   ├── project-scanner.md              # Phase 1: project scan
│   ├── research-extractor.md           # Phase 2: literature search & base model discovery
│   ├── project-analyzer.md             # Phase 3: novelty analysis + outline + user review
│   ├── paper-writer.md                 # Phase 4: paper writing
│   └── paper-reviewer.md               # Phase 5: review and refine
├── agent-workspace/                    # Output directory
│   ├── project-input/                  # Config (written by agent)
│   ├── analysis/                       # Intermediate artifacts
│   ├── output/                         # Final paper
│   └── templates/                      # Output templates
├── CLAUDE.md                           # Auto-read by Claude Code
├── SKILL.md                            # Usage reference
└── AGENTS.md                           # Agent architecture guide
```

---

## License

MIT
