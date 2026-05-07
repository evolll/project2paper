# Gemini CLI Install — project2paper

1. Clone and install:
   ```
   git clone https://github.com/your-org/project2paper.git ~/.gemini/project2paper
   pip install -e ~/.gemini/project2paper
   ```

2. Symlink skills:
   ```
   mkdir -p ~/.gemini/skills
   ln -sf ~/.gemini/project2paper/agents ~/.gemini/skills/project2paper
   ```

3. Use:
   ```
   project2paper /path/to/target-project
   ```
   Then tell Gemini CLI: "Read and follow AGENTS.md and SKILL.md from ~/.gemini/project2paper, then run the pipeline."
