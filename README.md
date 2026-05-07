# project2paper 📄

**Turn any codebase into a well-structured technical paper.**

A self-healing harness that enables LLMs to analyze any project and produce a publication-quality paper. Supports multiple lengths, tones, and focus areas.

```
  project2paper ./my-project --length long --tone academic --focus architecture

  ● Phase 1: project-scanner   → project structure mapped
  ● Phase 2: project-analyzer  → architecture analyzed
  ● Phase 3: research-extractor → insights extracted (focus=architecture)
  ● Phase 4: paper-writer      → paper drafted (length=long, tone=academic)
  ● Phase 5: paper-reviewer    → paper reviewed and refined
  │
  ✓ agent-workspace/output/paper.md — done
```

## Quick start

```bash
pip install -e .

# Interactive wizard — pick length, tone, format, language step by step
project2paper
# (default output: LaTeX)

# Short overview
project2paper /path/to/project --length short --tone blog

# Full academic paper
project2paper /path/to/project --length long --tone academic --format latex
```

Then tell your agent: "Run the project2paper pipeline on /path/to/project."

## Options

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--length` / `-L` | short, medium, long | medium | Paper depth |
| `--tone` / `-T` | academic, blog, technical-report, tutorial | academic | Writing style |
| `--focus` / `-F` | architecture, features, performance, full | full | Analysis emphasis |
| `--format` / `-f` | markdown, latex, html | markdown | Output format |
| `--language` / `-l` | zh-CN, ja-JP, etc. | — | Output language |

## Length presets

| Length | Words | Sections | Use case |
|--------|-------|----------|----------|
| short | 500-1K | 5 | Executive summary, quick overview |
| medium | 2K-4K | 8 | Standard docs (default) |
| long | 5K-10K | 11 | Publication, deep analysis |

## Tone presets

| Tone | Audience | Style |
|------|----------|-------|
| academic | Researchers, architects | Formal, third-person |
| blog | Developers, eng managers | Conversational, engaging |
| technical-report | Eng teams, stakeholders | Data-driven, factual |
| tutorial | Learners | Step-by-step, pedagogical |

## Architecture

- `install.md` — Setup and configuration
- `SKILL.md` — Day-to-day agent usage
- `AGENTS.md` — Agent architecture guide
- `src/project2paper/` — Core package (CLI, pipeline, helpers, templates)
- `agents/` — Agent prompt files for each pipeline phase
- `agent-workspace/` — Editable workspace (analysis, output, templates)

## Contributing

PRs welcome! Add agent prompts for domain-specific analysis, improve templates, or submit example papers.

## License

MIT
