"""Paper structure templates for different output formats."""

PAPER_STRUCTURE_MARKDOWN = {
    "sections": [
        {"title": "Title", "description": "Paper title, subtitle, author info, date"},
        {"title": "Abstract", "description": "Brief summary of the project, its purpose, and key findings"},
        {"title": "1. Introduction", "description": "Context, motivation, problem statement, project overview"},
        {"title": "2. Architecture Overview", "description": "High-level system architecture, tech stack, design philosophy"},
        {"title": "3. Core Components", "description": "Deep dive into major subsystems and modules"},
        {"title": "4. Key Design Decisions", "description": "Architectural choices, trade-offs, rationale"},
        {"title": "5. Data Flow & Interactions", "description": "How data moves through the system, API contracts"},
        {"title": "6. Implementation Highlights", "description": "Notable implementations, algorithms, patterns"},
        {"title": "7. Discussion", "description": "Lessons learned, known limitations, future work"},
        {"title": "8. Conclusion", "description": "Summary of contributions and impact"},
        {"title": "References", "description": "Related work, dependencies, acknowledgments"},
    ],
}


PAPER_STRUCTURE_LATEX = {
    "sections": [
        {"title": r"\title{} \author{} \date{}", "description": "Title page"},
        {"title": r"\begin{abstract}", "description": "Abstract"},
        {"title": r"\section{Introduction}", "description": "Introduction"},
        {"title": r"\section{Architecture}", "description": "Architecture overview"},
        {"title": r"\section{Core Components}", "description": "Component deep dive"},
        {"title": r"\section{Design Decisions}", "description": "Key decisions"},
        {"title": r"\section{Data Flow}", "description": "Data flow and interactions"},
        {"title": r"\section{Implementation}", "description": "Implementation details"},
        {"title": r"\section{Discussion}", "description": "Discussion"},
        {"title": r"\section{Conclusion}", "description": "Conclusion"},
        {"title": r"\bibliographystyle{plain} \bibliography{refs}", "description": "References"},
    ],
}


PAPER_STRUCTURE_HTML = {
    "sections": [
        {"title": "<h1>Title</h1>", "description": "Title and metadata"},
        {"title": "<section id='abstract'>", "description": "Abstract"},
        {"title": "<section id='introduction'>", "description": "Introduction"},
        {"title": "<section id='architecture'>", "description": "Architecture"},
        {"title": "<section id='components'>", "description": "Components"},
        {"title": "<section id='decisions'>", "description": "Design decisions"},
        {"title": "<section id='dataflow'>", "description": "Data flow"},
        {"title": "<section id='implementation'>", "description": "Implementation"},
        {"title": "<section id='discussion'>", "description": "Discussion"},
        {"title": "<section id='conclusion'>", "description": "Conclusion"},
        {"title": "<section id='references'>", "description": "References"},
    ],
}
