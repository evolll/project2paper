# project2paper — Agent Usage Skill

## How to use project2paper

project2paper takes a project path as input and generates a well-structured technical paper. The agent drives the full pipeline — you just provide the project.

### Quick start in any coding agent

```
Read and follow SKILL.md and AGENTS.md from /path/to/project2paper.
Then run the pipeline on /path/to/target-project.
```

### Interactive use

```bash
# 1. Analyze a project
project2paper /path/to/target-project --output paper.md

# 2. Tell your agent:
"Run the project2paper pipeline on /path/to/target-project"
```

The agent will:
1. Read AGENTS.md and SKILL.md
2. Read all agent prompt files in `agents/`
3. Execute the 5-phase pipeline
4. Deliver the paper to `agent-workspace/output/`

### Output format

```bash
# Markdown (default)
project2paper . --output paper.md

# LaTeX
project2paper /path/to/project --format latex

# HTML
project2paper /path/to/project --format html

# Specify language
project2paper /path/to/project --language zh-CN
```

### Pipeline phases (automatic)

| Phase | Agent | Input | Output |
|-------|-------|-------|--------|
| 1 | project-scanner | Project files | project-map.json |
| 2 | project-analyzer | project-map.json + source | architecture.json |
| 3 | research-extractor | analysis files + source | research-findings.json |
| 4 | paper-writer | all analysis | paper.{md/tex/html} |
| 5 | paper-reviewer | paper + source | paper-reviewed.{md/tex/html} |

### Important rules

1. **Never edit files inside `src/project2paper/`** — the core package is protected
2. **Agent-editable files** are in `agent-workspace/`:
   - `agent_helpers.py` — custom analysis helpers
   - `templates/` — output templates
3. **Intermediate analysis** lives in `agent-workspace/analysis/`
4. **Final output** lands in `agent-workspace/output/`
5. The agent writes what's missing. If a library isn't installed, the agent installs it. If a helper function doesn't exist, the agent writes it in `agent_helpers.py`.

### Design constraints

- The pipeline is **phase-sequential** — each phase depends on previous outputs
- Agents run **one at a time** (not concurrent), keeping context focused
- The paper-reviewer phase is mandatory — always review before declaring done
- If a phase fails, fix the issue and retry that phase, don't restart from scratch
