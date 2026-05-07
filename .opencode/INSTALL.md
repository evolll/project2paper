# OpenCode Install — project2paper

1. Clone the repo:
   ```
   git clone https://github.com/your-org/project2paper.git ~/.opencode/project2paper
   ```

2. Install the Python package:
   ```
   pip install -e ~/.opencode/project2paper
   ```

3. Symlink the skills (so OpenCode can find the agent prompts):
   ```
   mkdir -p ~/.opencode/skills
   ln -sf ~/.opencode/project2paper/agents ~/.opencode/skills/project2paper
   ```

4. Done. Now you can:
   ```
   project2paper /path/to/target-project
   ```
   Then paste the project path into OpenCode.

For agent integration:
```
Read ~/.opencode/project2paper/AGENTS.md and ~/.opencode/project2paper/SKILL.md
```
