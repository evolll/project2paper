# Pi Agent Install — project2paper

1. Clone and install:
   ```
   git clone https://github.com/your-org/project2paper.git ~/.pi/project2paper
   pip install -e ~/.pi/project2paper
   ```

2. Symlink skills:
   ```
   mkdir -p ~/.pi/skills
   ln -sf ~/.pi/project2paper/agents ~/.pi/skills/project2paper
   ```

3. Use:
   ```
   project2paper /path/to/target-project
   ```
   Then tell Pi Agent: "Read and follow AGENTS.md and SKILL.md from ~/.pi/project2paper, then run the pipeline."
