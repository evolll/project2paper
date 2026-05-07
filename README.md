# project2paper

**Turn any codebase into a well-structured technical paper.**

A self-healing harness that enables LLMs to analyze any project and produce a publication-quality paper.

```
Tell your agent: "Read AGENTS.md and run the project2paper pipeline on /path/to/project with --length long --tone academic --format latex"

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

Claude Code auto-discovers the plugin via `.claude-plugin/plugin.json`.

### 2. Generate the paper

In Claude Code, tell it:

```
Read AGENTS.md and run the project2paper pipeline on /path/to/your-project.
```

Want a specific length, tone, or format? Add options to the instruction:

```
Read AGENTS.md and run the project2paper pipeline on /path/to/your-project with:
  length=long, tone=academic, focus=architecture, format=latex, language=zh-CN
```

The agent writes `agent-workspace/project-input/config.json` with your choices, then executes the 5-phase pipeline. Everything lands in `agent-workspace/output/`.

### 3. Keep exploring

```
# Short blog-style overview
...pipeline on /path with: length=short, tone=blog

# Deep architecture analysis
...pipeline on /path with: length=long, tone=academic, focus=architecture, format=latex

# Performance report for stakeholders
...pipeline on /path with: length=medium, tone=technical-report, focus=performance

# Tutorial for new team members
...pipeline on /path with: length=long, tone=tutorial, focus=features

# Generate in Chinese
...pipeline on /path with: language=zh-CN, format=latex
```

---

## Options

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `length` | short, medium, long | medium | Paper depth |
| `tone` | academic, blog, technical-report, tutorial | academic | Writing style |
| `focus` | architecture, features, performance, full | full | Analysis emphasis |
| `format` | markdown, latex, html | latex | Output format |
| `language` | zh-CN, ja-JP, etc. | en | Output language |

### Length

| Length | Words | Sections | Use case |
|--------|-------|----------|----------|
| short | 500-1K | 5 | Executive summary |
| medium | 2K-4K | 8 | Standard documentation |
| long | 5K-10K | 11 | Publication, deep analysis |

### Tone

| Tone | Style | Audience |
|------|-------|----------|
| academic | Formal, third-person | Researchers, architects |
| blog | Conversational, engaging | Developers |
| technical-report | Data-driven, factual | Stakeholders |
| tutorial | Step-by-step, pedagogical | Learners |

### Focus

| Focus | Emphasis |
|-------|----------|
| architecture | System design, layers, relationships |
| features | User-facing capabilities |
| performance | Benchmarks, scalability |
| full | Balanced coverage |

---

## Architecture

```
project2paper/
├── CLAUDE.md                 # Auto-read at Claude Code session start
├── SKILL.md                  # Agent usage instructions
├── AGENTS.md                 # Agent architecture guide
├── agents/                   # Agent prompts (one per pipeline phase)
│   ├── project-scanner.md
│   ├── project-analyzer.md
│   ├── research-extractor.md
│   ├── paper-writer.md
│   └── paper-reviewer.md
├── .claude-plugin/           # Claude Code plugin registration
├── agent-workspace/          # Agent-editable workspace
│   ├── project-input/        # Config written by the agent
│   ├── analysis/             # Intermediate analysis artifacts
│   ├── output/               # Final paper output
│   └── templates/            # Output format templates
```

---

## Multi-Platform

| Platform | How to use |
|----------|-----------|
| Claude Code | Clone, auto-discovered. Tell agent to read AGENTS.md |
| Codex / OpenCode / Cursor / Copilot / Gemini CLI | Clone the repo, then tell your agent: "Read and follow SKILL.md and AGENTS.md from /path/to/project2paper, then run the pipeline on /path/to/target-project." |

---

## License

MIT
