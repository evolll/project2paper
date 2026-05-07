# project2paper

**Turn any codebase into a well-structured technical paper.**

A self-healing harness that enables LLMs (Claude Code, Codex, OpenCode, Cursor, Copilot, Gemini CLI, and more) to analyze any project and produce a publication-quality paper. Supports multiple lengths, tones, focus areas, languages, and output formats.

```
  project2paper ./my-project --length long --tone academic --focus architecture --format latex

  ● Phase 1: project-scanner   → project structure mapped
  ● Phase 2: project-analyzer  → architecture analyzed
  ● Phase 3: research-extractor → insights extracted
  ● Phase 4: paper-writer      → paper drafted
  ● Phase 5: paper-reviewer    → paper reviewed and refined
  │
  ✓ agent-workspace/output/paper.tex — ready for arXiv / conference submission
```

---

## Quick Start

### 1. Install the plugin

```bash
git clone https://github.com/evolll/project2paper.git ~/.claude/plugins/project2paper
pip install -e ~/.claude/plugins/project2paper
```

The plugin is auto-discovered by Claude Code via `.claude-plugin/plugin.json`. No further setup needed.

### 2. Configure the project

```bash
project2paper /path/to/your-project --length long --tone academic --format latex
```

Or use the interactive wizard (no arguments):

```bash
project2paper
```

You'll be asked step by step: project path, paper length, tone, focus area, output format, and language.

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--length` / `-L` | short, medium, long | medium | Paper depth |
| `--tone` / `-T` | academic, blog, technical-report, tutorial | academic | Writing style |
| `--focus` / `-F` | architecture, features, performance, full | full | Analysis emphasis |
| `--format` / `-f` | markdown, latex, html | latex | Output format |
| `--language` / `-l` | zh-CN, ja-JP, etc. | — | Output language |

### 3. Generate the paper

In Claude Code, run:

```
Read AGENTS.md and run the project2paper pipeline.
```

A 5-phase agent pipeline scans your project, analyzes architecture, extracts research insights, writes the paper, and reviews it. All artifacts are saved to `agent-workspace/`.

### 4. Keep exploring

```bash
# Short blog-style overview
project2paper /path/to/project --length short --tone blog

# Deep architecture analysis for a conference paper
project2paper /path/to/project --length long --tone academic --focus architecture --format latex

# Performance report for stakeholders
project2paper /path/to/project --length medium --tone technical-report --focus performance

# Tutorial for new team members
project2paper /path/to/project --length long --tone tutorial --focus features

# Generate in Chinese
project2paper /path/to/project --language zh-CN --format latex
```

---

## CLI Reference

### Length presets

| Length | Words | Sections | Use case |
|--------|-------|----------|----------|
| short | 500-1K | 5 | Executive summary, quick overview |
| medium | 2K-4K | 8 | Standard documentation (default) |
| long | 5K-10K | 11 | Publication, deep analysis |

### Tone presets

| Tone | Audience | Style |
|------|----------|-------|
| academic | Researchers, architects | Formal, third-person |
| blog | Developers, eng managers | Conversational, engaging |
| technical-report | Eng teams, stakeholders | Data-driven, factual |
| tutorial | Learners | Step-by-step, pedagogical |

### Focus presets

| Focus | Emphasis |
|-------|----------|
| architecture | System design, layers, component relationships |
| features | User-facing capabilities and workflows |
| performance | Benchmarks, scalability, bottlenecks |
| full | Balanced coverage across all aspects |

---

## Architecture

- `install.md` — Setup and configuration
- `CLAUDE.md` — Claude Code project overview (auto-read at session start)
- `SKILL.md` — Day-to-day agent usage instructions
- `AGENTS.md` — Agent architecture guide
- `src/project2paper/` — Core Python package (CLI, pipeline, helpers, templates)
- `agents/` — Agent prompt files for each pipeline phase
- `.claude-plugin/plugin.json` — Claude Code plugin registration
- `agent-workspace/` — Editable workspace (analysis, output, templates)

---

## Multi-Platform Support

### Claude Code (Native)

The plugin is auto-discovered when cloned. Run `pip install -e .` to install the CLI, then tell Claude Code:

```
Read AGENTS.md and run the project2paper pipeline.
```

### Codex / OpenCode / Cursor / Gemini CLI / Copilot / Others

Clone the repo and install the Python package, then tell your agent:

```
Read and follow SKILL.md and AGENTS.md from /path/to/project2paper, then run the pipeline on /path/to/target-project.
```

---

## Contributing

PRs welcome! Add agent prompts for domain-specific analysis, improve output templates, or submit example papers.

---

## License

MIT
