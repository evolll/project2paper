# Changelog

## [0.3.1] — 2026-05-22

### Added
- `--template` CLI argument for LaTeX style selection (`article`, `ieee`, `acm`)
- Interactive prompt for template style selection when format is LaTeX
- `template_style` field in default config
- CHANGELOG.md to track project history

### Fixed
- Missing `--template` argument documentation in README and SKILL files
- Agent helpers now properly register template style in config defaults

## [0.3.0] — 2026-05-21

### Added
- Interactive mode (`--interactive`) with phase-by-phase user interaction
- Novelty classification (`--novelty`) with 4-level inline markers (Novel, Improved, Existing, Baseline)
- Base project comparison (`--base`) for automatic contribution detection
- Per-chapter LaTeX output with `\input{}` (no forced page breaks)
- Placeholder support: `\todo{}` for text, `\missingfigure{}` for diagrams
- Reference paper support (arXiv IDs, DOIs, PDFs) with BibTeX generation
- Novelty summary table in output
- 6-pipeline overview images

### Changed
- Full README rewrite with comprehensive documentation
- Pipeline reordered to: config → scan → research → analyze → write → review
- Academic tone as default output style
- Agent prompts restructured for clarity

## [0.2.0] — 2026-05-18

### Added
- Initial 5-phase agent pipeline
- LaTeX, Markdown, and HTML output support
- Interactive configuration phase
- Project scanning and language detection
- Basic paper generation with agent prompts
- Claude Code plugin registration (v0.2.0)

## [0.1.0] — 2026-05-15

### Added
- Initial plugin structure
- Agent prompt framework
- Basic README and documentation
