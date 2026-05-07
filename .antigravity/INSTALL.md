# Antigravity Install — project2paper

1. Clone and install:
   ```
   git clone https://github.com/your-org/project2paper.git ~/.antigravity/project2paper
   pip install -e ~/.antigravity/project2paper
   ```

2. Symlink skills:
   ```
   mkdir -p ~/.antigravity/skills
   ln -sf ~/.antigravity/project2paper/agents ~/.antigravity/skills/project2paper
   ```

3. Use:
   ```
   project2paper /path/to/target-project
   ```
   Then tell Antigravity: "Read and follow AGENTS.md and SKILL.md from ~/.antigravity/project2paper, then run the pipeline."
