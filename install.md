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
project2paper /path/to/your/project

# Then give the agent the project path — it will do the rest.
```

## Environment (optional)

Copy `.env.example` to `.env` and configure:

| Variable | Description | Default |
|----------|-------------|---------|
| `PROJECT2PAPER_AGENT_WORKSPACE` | Custom workspace path | `./agent-workspace` |
| `PROJECT2PAPER_DEFAULT_FORMAT` | Default output format | `markdown` |
| `PROJECT2PAPER_LANGUAGE` | Output language | `en` |

## Troubleshooting

- **"command not found: project2paper"** → Make sure the Python environment is activated (`source .venv/bin/activate`)
- **Permission errors** → The project2paper workspace needs write access to `agent-workspace/output/`
- **Large projects** → For projects with 10K+ files, the scanner may take a minute. This is normal.
