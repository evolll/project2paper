# Install project2paper

## Prerequisites
- Python 3.11+
- `uv` (recommended) or `pip`

## Setup

### 1. Clone and install

```bash
git clone https://github.com/your-org/project2paper.git
cd project2paper

# Option A: uv (recommended)
uv sync

# Option B: pip
pip install -e .
```

### 2. Verify

```bash
project2paper --version
```

### 3. Done

```bash
# Analyze any project:
project2paper /path/to/your/project --length medium --tone academic

# Then give the agent the project path — it will do the rest.
```

## Environment (optional)

Copy `.env.example` to `.env` and configure:

| Variable | Description | Default |
|----------|-------------|---------|
| `PROJECT2PAPER_AGENT_WORKSPACE` | Custom workspace path | `./agent-workspace` |
| `PROJECT2PAPER_DEFAULT_LENGTH` | Default paper length | `medium` |
| `PROJECT2PAPER_DEFAULT_TONE` | Default writing tone | `academic` |
| `PROJECT2PAPER_DEFAULT_FOCUS` | Default focus area | `full` |
| `PROJECT2PAPER_DEFAULT_FORMAT` | Default output format | `markdown` |
| `PROJECT2PAPER_LANGUAGE` | Output language | `en` |

## Troubleshooting

- **"command not found: project2paper"** → Activate the Python environment (`source .venv/bin/activate`)
- **Permission errors** → Workspace needs write access to `agent-workspace/output/`
- **Large projects** → 10K+ files may take a minute. Consider `--length short` for a quick first pass.
