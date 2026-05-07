# project2paper — Agent Usage Skill

## How to use project2paper

project2paper takes a project path and generates a well-structured technical paper. The agent drives the full pipeline.

### Quick start

```
Read and follow SKILL.md and AGENTS.md from /path/to/project2paper.
Then run the pipeline on /path/to/target-project.
```

### Interactive mode (wizard)

Run without arguments to enter the interactive wizard — it will ask you step by step:

```bash
project2paper
```

Or force it with `-i`:

```bash
project2paper -i
```

You'll be prompted to choose:
1. **Project path** — browse or type
2. **Paper length** — short / medium / long
3. **Writing tone** — academic / blog / technical-report / tutorial
4. **Analysis focus** — architecture / features / performance / full
5. **Output format** — markdown / latex / html (default: **latex**)
6. **Language** — 11 languages including zh-CN, ja-JP, ko-KR

### Non-interactive (CLI flags)

```bash
# Quick overview (short paper, blog tone)
project2paper /path/to/target-project --length short --tone blog

# Full academic paper
project2paper /path/to/target-project --length long --tone academic --focus architecture

# Technical report focused on performance
project2paper /path/to/target-project --length medium --tone technical-report --focus performance

# Tutorial for new developers
project2paper /path/to/target-project --length long --tone tutorial --focus features

# Chinese output
project2paper /path/to/target-project --language zh-CN --format latex
```

Then tell your agent: "Run the project2paper pipeline on /path/to/target-project."

### Options

| Flag | Values | Default | Description |
|------|--------|---------|-------------|
| `--length` / `-L` | short, medium, long | medium | Paper depth and word count |
| `--tone` / `-T` | academic, blog, technical-report, tutorial | academic | Writing style |
| `--focus` / `-F` | architecture, features, performance, full | full | Analysis emphasis |
| `--format` / `-f` | markdown, latex, html | markdown | Output format |
| `--language` / `-l` | zh-CN, ja-JP, etc. | — | Output language |
| `--output` / `-o` | path | auto | Output file path |

### Length presets

| Length | Words | Sections | Best for |
|--------|-------|----------|----------|
| **short** | 500-1K | 5 | Quick overview, executive summary |
| **medium** | 2K-4K | 8 | Standard documentation (default) |
| **long** | 5K-10K | 11 | Publication, deep analysis |

### Tone presets

| Tone | Style | Audience |
|------|-------|----------|
| **academic** | Formal, objective, third-person | Researchers, architects |
| **blog** | Conversational, engaging | Developers, eng managers |
| **technical-report** | Direct, data-driven, factual | Eng teams, stakeholders |
| **tutorial** | Instructional, step-by-step | Developers learning the codebase |

### Pipeline phases

| Phase | Agent | Input | Output |
|-------|-------|-------|--------|
| 1 | project-scanner | Project files | project-map.json |
| 2 | project-analyzer | project-map.json + source | architecture.json |
| 3 | research-extractor | analysis files + source | research-findings.json |
| 4 | paper-writer | all analysis + config (length/tone/focus) | paper.{md/tex/html} |
| 5 | paper-reviewer | paper + source | paper-reviewed.{md/tex/html} |

### Important rules

1. **Never edit `src/project2paper/`** — core package is protected
2. **Agent-editable**: `agent-workspace/agent_helpers.py`, `agent-workspace/templates/`
3. **Intermediate analysis**: `agent-workspace/analysis/`
4. **Final output**: `agent-workspace/output/`
5. The agent writes what's missing. If a helper doesn't exist, the agent writes it.

### Design constraints

- Pipeline is **phase-sequential**
- Agents run **one at a time**
- Paper-reviewer phase is **mandatory**
- If a phase fails, fix and retry that phase only
