# VS Code + GitHub Copilot Install — project2paper

1. Clone the repo to a known location:
   ```
   git clone https://github.com/your-org/project2paper.git ~/project2paper
   pip install -e ~/project2paper
   ```

2. In VS Code, tell Copilot:
   ```
   Read and follow AGENTS.md and SKILL.md from ~/project2paper, then run the pipeline on the current project.
   ```

3. Or add to your project's `.vscode/settings.json`:
   ```json
   {
     "github.copilot.chat.agents": {
       "project2paper": {
         "path": "~/project2paper/agents"
       }
     }
   }
   ```
