"""Paper structure templates for different lengths, tones, and focus areas."""

# ─── Length presets ─────────────────────────────────────────────────

LENGTH_PRESETS = {
    "short": {
        "label": "Short Paper",
        "word_count": "500-1000 words",
        "sections": 5,
        "code_depth": "minimal",
        "diagram_depth": "minimal",
        "description": "Quick overview. Best for a fast understanding.",
    },
    "medium": {
        "label": "Medium Paper",
        "word_count": "2000-4000 words",
        "sections": 8,
        "code_depth": "moderate",
        "diagram_depth": "moderate",
        "description": "Balanced depth. Default recommendation.",
    },
    "long": {
        "label": "Long Paper",
        "word_count": "5000-10000 words",
        "sections": 11,
        "code_depth": "deep",
        "diagram_depth": "deep",
        "description": "Exhaustive analysis. Best for documentation or publication.",
    },
}

# ─── Tone descriptions ──────────────────────────────────────────────

TONE_GUIDE = {
    "academic": {
        "voice": "Formal, objective, third-person",
        "style": "Problem → Method → Results → Discussion",
        "audience": "Researchers, architects, technical leads",
        "citation_style": "Formal references with related work section",
        "example_phrases": "We propose … The results demonstrate … This work contributes …",
    },
    "blog": {
        "voice": "Conversational, first-person, engaging",
        "style": "Hook → Story → Insights → Takeaways",
        "audience": "Developers, engineering managers",
        "citation_style": "Inline links and mentions",
        "example_phrases": "Here's what we built … The tricky part was … You might wonder …",
    },
    "technical-report": {
        "voice": "Direct, factual, data-driven",
        "style": "Context → Data → Analysis → Recommendations",
        "audience": "Engineering teams, stakeholders",
        "citation_style": "Minimal — focus on data and benchmarks",
        "example_phrases": "Benchmarks show … Implementation details … Measured impact …",
    },
    "tutorial": {
        "voice": "Instructional, pedagogical, step-by-step",
        "style": "Goal → Prerequisites → Walkthrough → Summary",
        "audience": "Developers learning the codebase",
        "citation_style": "Only for further reading",
        "example_phrases": "First, let's … Notice how … Try this yourself …",
    },
}

# ─── Focus areas ────────────────────────────────────────────────────

FOCUS_GUIDE = {
    "architecture": {
        "emphasis": "System design, layers, components, relationships",
        "deemphasize": "Feature details, line-by-line implementation",
        "sections_boost": ["Architecture Overview", "Key Design Decisions", "Data Flow"],
    },
    "features": {
        "emphasis": "What the project does, user-facing capabilities",
        "deemphasize": "Internal plumbing, low-level implementation",
        "sections_boost": ["Core Components", "Implementation Highlights", "Introduction"],
    },
    "performance": {
        "emphasis": "Benchmarks, optimizations, scalability, bottlenecks",
        "deemphasize": "Feature breadth, UI details",
        "sections_boost": ["Implementation Highlights", "Discussion", "Data Flow"],
    },
    "full": {
        "emphasis": "Balanced coverage across all aspects",
        "deemphasize": "None",
        "sections_boost": [],
    },
}

# ─── Section structures per length ──────────────────────────────────

SECTIONS_BY_LENGTH = {
    "short": [
        {"id": "title", "title": "Title", "description": "Title, subtitle, one-line tagline"},
        {"id": "abstract", "title": "Abstract", "description": "50-100 word summary"},
        {"id": "introduction", "title": "1. Introduction", "description": "Problem statement and project overview (1-2 paragraphs)"},
        {"id": "architecture", "title": "2. Architecture", "description": "High-level architecture, tech stack, key insight (1 diagram)"},
        {"id": "key_findings", "title": "3. Key Findings", "description": "Most important takeaways and decisions"},
        {"id": "conclusion", "title": "4. Conclusion", "description": "Summary and next steps"},
    ],
    "medium": [
        {"id": "title", "title": "Title", "description": "Title, subtitle, author info"},
        {"id": "abstract", "title": "Abstract", "description": "150-250 word summary"},
        {"id": "introduction", "title": "1. Introduction", "description": "Context, motivation, problem statement"},
        {"id": "architecture", "title": "2. Architecture Overview", "description": "High-level design, ASCII diagram, tech stack"},
        {"id": "components", "title": "3. Core Components", "description": "Major subsystems and their roles"},
        {"id": "decisions", "title": "4. Key Design Decisions", "description": "Architectural choices and trade-offs"},
        {"id": "discussion", "title": "5. Discussion", "description": "Lessons learned, limitations, future work"},
        {"id": "conclusion", "title": "6. Conclusion", "description": "Summary of contributions"},
        {"id": "references", "title": "References", "description": "Related work and acknowledgments"},
    ],
    "long": [
        {"id": "title", "title": "Title", "description": "Full title page with subtitle, author, date"},
        {"id": "abstract", "title": "Abstract", "description": "200-300 word comprehensive summary"},
        {"id": "introduction", "title": "1. Introduction", "description": "Context, motivation, problem statement, project overview, paper roadmap"},
        {"id": "architecture", "title": "2. Architecture Overview", "description": "High-level design, philosophy, layers, tech stack with justification"},
        {"id": "components", "title": "3. Core Components", "description": "Deep dive into each major subsystem with code snippets"},
        {"id": "decisions", "title": "4. Key Design Decisions", "description": "Major choices, alternatives considered, trade-off analysis"},
        {"id": "dataflow", "title": "5. Data Flow & Interactions", "description": "Data movement, API contracts, event flows, sequence diagrams"},
        {"id": "highlights", "title": "6. Implementation Highlights", "description": "Algorithms, design patterns, optimization techniques"},
        {"id": "discussion", "title": "7. Discussion", "description": "Lessons learned, known limitations, future work, comparison"},
        {"id": "conclusion", "title": "8. Conclusion", "description": "Contributions summary, impact, broader implications"},
        {"id": "references", "title": "References", "description": "Related work, dependencies, acknowledgments"},
    ],
}

SECTIONS_BY_LENGTH_LATEX = {
    "short": [
        {"title": r"\title{} \author{} \date{}"},
        {"title": r"\begin{abstract}"},
        {"title": r"\section{Introduction}"},
        {"title": r"\section{Architecture}"},
        {"title": r"\section{Key Findings}"},
        {"title": r"\section{Conclusion}"},
    ],
    "medium": [
        {"title": r"\title{} \author{} \date{}"},
        {"title": r"\begin{abstract}"},
        {"title": r"\section{Introduction}"},
        {"title": r"\section{Architecture}"},
        {"title": r"\section{Core Components}"},
        {"title": r"\section{Design Decisions}"},
        {"title": r"\section{Discussion}"},
        {"title": r"\section{Conclusion}"},
        {"title": r"\bibliographystyle{plain} \bibliography{refs}"},
    ],
    "long": [
        {"title": r"\title{} \author{} \date{}"},
        {"title": r"\begin{abstract}"},
        {"title": r"\section{Introduction}"},
        {"title": r"\section{Architecture}"},
        {"title": r"\section{Core Components}"},
        {"title": r"\section{Design Decisions}"},
        {"title": r"\section{Data Flow and Interactions}"},
        {"title": r"\section{Implementation Highlights}"},
        {"title": r"\section{Discussion}"},
        {"title": r"\section{Conclusion}"},
        {"title": r"\bibliographystyle{plain} \bibliography{refs}"},
    ],
}

SECTIONS_BY_LENGTH_HTML = {
    "short": [
        {"title": "<h1>Title</h1>"},
        {"title": "<section id='abstract'>Abstract"},
        {"title": "<section id='introduction'>Introduction"},
        {"title": "<section id='architecture'>Architecture"},
        {"title": "<section id='findings'>Key Findings"},
        {"title": "<section id='conclusion'>Conclusion"},
    ],
    "medium": [
        {"title": "<h1>Title</h1>"},
        {"title": "<section id='abstract'>Abstract"},
        {"title": "<section id='introduction'>Introduction"},
        {"title": "<section id='architecture'>Architecture"},
        {"title": "<section id='components'>Components"},
        {"title": "<section id='decisions'>Design Decisions"},
        {"title": "<section id='discussion'>Discussion"},
        {"title": "<section id='conclusion'>Conclusion"},
        {"title": "<section id='references'>References"},
    ],
    "long": [
        {"title": "<h1>Title</h1>"},
        {"title": "<section id='abstract'>Abstract"},
        {"title": "<section id='introduction'>Introduction"},
        {"title": "<section id='architecture'>Architecture"},
        {"title": "<section id='components'>Components"},
        {"title": "<section id='decisions'>Design Decisions"},
        {"title": "<section id='dataflow'>Data Flow"},
        {"title": "<section id='highlights'>Implementation Highlights"},
        {"title": "<section id='discussion'>Discussion"},
        {"title": "<section id='conclusion'>Conclusion"},
        {"title": "<section id='references'>References"},
    ],
}
