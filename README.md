# project2paper 📄

**Turn any codebase into a well-structured technical paper.**

A self-healing harness that enables LLMs to analyze any project and produce a publication-quality paper. One command to start, a 5-phase agent pipeline does the rest.

```
  ● agent: "analyze this project and write a paper"
  │
  ● agents/project-scanner.md → project structure mapped
  ● agents/project-analyzer.md → architecture analyzed
  ● agents/research-extractor.md → novel insights extracted
  ● agents/paper-writer.md → paper drafted
  ● agents/paper-reviewer.md → paper reviewed and refined
  │
  ✓ agent-workspace/output/paper.md — done
```

## Quick start

```bash
# Install
pip install -e .

# Run — point at any project
project2paper /path/to/your-project --output paper.md
```

Then tell your agent: "Run the project2paper pipeline on /path/to/your-project."

The agent reads `agents/` and executes the 5-phase pipeline. Output lands in `agent-workspace/output/`.

## Features

- **Multi-format output** — Markdown, LaTeX, or HTML
- **Multi-language** — Generate papers in any language
- **5-phase pipeline** — Scan → Analyze → Research → Write → Review
- **Self-healing** — The agent writes what's needed during execution
- **Project-agnostic** — Works with any language, framework, or project size

## Architecture (~300 lines across core files)

- `install.md` — Setup and configuration
- `SKILL.md` — Day-to-day agent usage
- `AGENTS.md` — Agent architecture guide
- `src/project2paper/` — Protected core package (CLI, pipeline, helpers, templates)
- `agents/` — Agent prompt files for each pipeline phase
- `agent-workspace/` — Editable workspace (analysis, output, templates)

## Contributing

PRs welcome! The best way to help:
- **Add agent prompts** for domain-specific analysis (e.g., `agents/research-extractor-ml.md` for ML projects)
- **Improve templates** in `agent-workspace/templates/`
- **Submit generated papers** as examples in `examples/`

## How it differs from Understand-Anything

| | Understand-Anything | project2paper |
|---|---|---|
| **Goal** | Interactive knowledge graph | Publication-quality paper |
| **Output** | Graph visualization + search | Markdown/LaTeX/HTML document |
| **Pipeline** | 6 agents for graph building | 5 agents for paper generation |
| **Audience** | Developers exploring code | Technical readers |
| **Persistence** | Committable graph JSON | Ready-to-publish document |

## License

MIT
