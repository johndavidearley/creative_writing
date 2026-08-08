# Creative Writing Workspace

This repository is a working system for developing prose fiction through dramatic design: character desire, conflict, consequence, theme, and revision pressure.

The current active projects are:

- `Black Banner Academy`: military academy science fiction / political coming-of-age thriller.
- `The Veil War`: political military science fiction / refugee-fleet and carrier-war drama.

## Repository Map

- `AGENTS.md`: the governing craft contract for writing, revising, and evaluating story material in this repo.
- `manuscripts/`: current manuscript drafts and project-level story briefs.
- `reports/`: exploratory planning reports, alternate structures, beat outlines, and chapter-one variants.
- `skills/`: reusable craft workflows for drafting, story audits, scene audits, and dialogue polish.
- `templates/`: reusable story brief, character card, scene card, and revision report formats.
- `scripts/`: local utilities for converting DOCX files to Markdown and applying one-off DOCX revision passes.

## Current Draft Direction

The manuscript files are the current working drafts. The report files preserve alternate options and earlier exploration.

- `manuscripts/black-banner-academy.md` currently follows the "Covert Recruitment Pipeline" shape.
- `manuscripts/veil-war.md` currently follows the "Refugee Fleet War" shape.

## Common Workflows

Use the templates when starting or reshaping story material:

- Start a new story or major arc from `templates/story-brief.md`.
- Design a character with `templates/character-card.md`.
- Pressure-test a scene with `templates/scene-card.md`.
- Produce a revision diagnosis with `templates/revision-report.md`.

Use the skills as process guides:

- `skills/creative-writing-drafting.md` for new scenes, chapters, premises, and outlines.
- `skills/story-audit.md` for manuscript, chapter, treatment, or outline evaluation.
- `skills/scene-audit.md` for scene-level diagnosis and rewrite planning.
- `skills/dialogue-polish.md` for subtext, voice, and conflict passes.

## Script Usage

Convert a DOCX manuscript to Markdown:

```bash
python3 scripts/docx_to_markdown.py input.docx output.md
```

Apply the EOTLL report revision pass to a DOCX and export both DOCX and Markdown:

```bash
python3 scripts/apply_eotll_report_changes.py input.docx --out-docx /tmp/EOTLL.report-revision.docx --out-md manuscripts/EOTLL.report-revision.md
```

The EOTLL script is story-specific. It expects anchor text from the source document and will fail if that text is not present.
