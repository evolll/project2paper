# project2paper

**Turn any codebase into a well-structured technical paper.**

A Claude Code plugin that analyzes any project and produces a publication-quality paper. 5-phase pipeline: scan → analyze → research → write → review.

```
/project2paper /path/to/project --length long --tone academic --format latex

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

### 1. Clone

```bash
git clone https://github.com/evolll/project2paper.git ~/.claude/plugins/project2paper
```

Auto-discovered by Claude Code via `.claude-plugin/plugin.json`.

### 2. Run

In Claude Code:

```
/project2paper /path/to/your-project
```

### 3. Customize

```
/project2paper /path/to/your-project --length long --tone academic --focus architecture --format latex --language zh-CN
```

---

## Options

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `--length` | short, medium, long | medium | short (500-1K words), medium (2K-4K), long (5K-10K) |
| `--tone` | academic, blog, technical-report, tutorial | academic | Writing style and voice |
| `--focus` | architecture, features, performance, full | full | What to emphasize |
| `--format` | markdown, latex, html | latex | Output format |
| `--language` | zh-CN, ja-JP, etc. | en | Output language |

### Length

| Length | Words | Sections | Best for |
|--------|-------|----------|----------|
| short | 500-1K | 5 | Executive summary, quick overview |
| medium | 2K-4K | 8 | Standard documentation |
| long | 5K-10K | 11 | Publication, deep analysis |

### Tone

| Tone | Style | Audience |
|------|-------|----------|
| academic | Formal, third-person | Researchers, architects |
| blog | Conversational, engaging | Developers |
| technical-report | Data-driven, factual | Stakeholders |
| tutorial | Step-by-step, pedagogical | Learners |

---

## How it works

```
/project2paper /my-project --length long --tone academic

  ┌─ Phase 1 ──────────────────────────────┐
  │  agent/project-scanner.md              │
  │  → walks directory, catalogs files     │
  │  → detects language, framework, deps   │
  │  → writes project-map.json             │
  └────────────────────────────────────────┘
                     ↓
  ┌─ Phase 2 ──────────────────────────────┐
  │  agent/project-analyzer.md             │
  │  → reads key source files              │
  │  → maps architecture, layers, flows    │
  │  → writes architecture.json            │
  └────────────────────────────────────────┘
                     ↓
  ┌─ Phase 3 ──────────────────────────────┐
  │  agent/research-extractor.md           │
  │  → identifies novel insights           │
  │  → extracts decisions, trade-offs      │
  │  → writes research-findings.json       │
  └────────────────────────────────────────┘
                     ↓
  ┌─ Phase 4 ──────────────────────────────┐
  │  agent/paper-writer.md                 │
  │  → uses length/tone/focus from config  │
  │  → generates paper in specified format │
  │  → writes output/paper.tex             │
  └────────────────────────────────────────┘
                     ↓
  ┌─ Phase 5 ──────────────────────────────┐
  │  agent/paper-reviewer.md               │
  │  → verifies claims against source      │
  │  → checks length/tone/focus compliance │
  │  → writes output/paper-reviewed.tex    │
  └────────────────────────────────────────┘
```

---

## Project Structure

```
project2paper/
├── .claude-plugin/plugin.json     # Plugin registration
├── skills/
│   └── project2paper/SKILL.md     # /project2paper command
├── agents/
│   ├── project-scanner.md         # Phase 1
│   ├── project-analyzer.md        # Phase 2
│   ├── research-extractor.md      # Phase 3
│   ├── paper-writer.md            # Phase 4
│   └── paper-reviewer.md          # Phase 5
├── agent-workspace/               # Output directory
│   ├── project-input/             # Config (written by agent)
│   ├── analysis/                  # Intermediate artifacts
│   ├── output/                    # Final paper
│   └── templates/                 # Output templates
├── CLAUDE.md                      # Auto-read by Claude Code
├── SKILL.md                       # Usage reference
└── AGENTS.md                      # Agent architecture guide
```

---

## License

MIT
