# Codex Install — project2paper

1. Clone and install:
   ```
   git clone https://github.com/your-org/project2paper.git ~/.codex/project2paper
   pip install -e ~/.codex/project2paper
   ```

2. Symlink skills:
   ```
   mkdir -p ~/.codex/skills
   ln -sf ~/.codex/project2paper/agents ~/.codex/skills/project2paper
   ```

3. Use:
   ```
   project2paper /path/to/target-project
   ```
   Then tell Codex: "Read and follow AGENTS.md and SKILL.md from ~/.codex/project2paper, then run the pipeline."
