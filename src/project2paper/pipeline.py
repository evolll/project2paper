"""Pipeline orchestrator — describes the multi-agent paper generation pipeline.

This file documents the pipeline phases. The actual orchestration is driven
by the agent reading agent prompt files in agents/.
"""

PIPELINE_PHASES = [
    {
        "phase": 1,
        "name": "project-scanner",
        "description": "Discover files, detect languages, frameworks, and map project structure.",
        "agent": "agents/project-scanner.md",
        "output": "agent-workspace/analysis/project-map.json",
    },
    {
        "phase": 2,
        "name": "project-analyzer",
        "description": "Deep analysis of architecture, features, data flow, and design patterns.",
        "agent": "agents/project-analyzer.md",
        "output": "agent-workspace/analysis/architecture.json",
    },
    {
        "phase": 3,
        "name": "research-extractor",
        "description": "Extract novel insights, key decisions, trade-offs, and lessons learned.",
        "agent": "agents/research-extractor.md",
        "output": "agent-workspace/analysis/research-findings.json",
    },
    {
        "phase": 4,
        "name": "paper-writer",
        "description": "Generate the paper from all gathered analysis and research.",
        "agent": "agents/paper-writer.md",
        "output": "agent-workspace/output/paper.md",
    },
    {
        "phase": 5,
        "name": "paper-reviewer",
        "description": "Review paper for completeness, accuracy, and quality. Refine if needed.",
        "agent": "agents/paper-reviewer.md",
        "output": "agent-workspace/output/paper-reviewed.md",
    },
]
