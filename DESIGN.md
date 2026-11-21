# Design plan — EnZ0's Homepage

Made with Anthropic's `frontend-design` skill (`.claude/skills/frontend-design/`).
Subject: a Shenzhen University CS student's personal notebook — pattern-mining
papers, course notes and programming notes, kept in Chinese and English.
Audience: classmates, teachers and the author himself, mostly reading long
notes. The page's one job: make long notes easy to read and easy to find.

## Tokens

Color (boldness spent in one place: the SZU burgundy)
- SZU burgundy `#7E0725` — primary. Already the site's `themeColor` and
  Shenzhen University's colour; it is the one memorable element.
- Burgundy deep `#5E051B` — hover / pressed state for the primary.
- Ink `#211D1F` — body text.
- Paper `#FFFFFF` — page background.
- Stone `#F4F4F2` — sidebar, code and quote background. A cool neutral,
  deliberately not a warm cream.
- Line `#E2DEDB` — dividers and table borders.
- Pine `#28544A` — focus ring only, so keyboard focus never relies on the
  burgundy alone.

Type
- Headings: `Noto Serif SC`, `Songti SC`, serif — gives the Chinese notes an
  academic voice and makes type itself part of the design.
- Body: `Noto Sans SC`, `PingFang SC`, sans-serif — long-form Chinese
  reading, line length capped near 72 characters, line-height 1.8.
- Code: `JetBrains Mono`, `Fira Code`, monospace — for code only.

Layout
- Left-aligned reading column, max-width 880px, generous side padding.
- Sidebar 280px on stone, app name in serif burgundy, active page marked
  with a burgundy left bar instead of colour alone.
- Cover: serif title at large scale over the existing stair photo, one solid
  burgundy button (GitHub) and one outline button (开始阅读).

## Review against the generic defaults

The old `custom.css` was the template the skill warns about, so it was
rewritten rather than patched:
- It used Inter for everything — a named default in the skill — and set
  headings and the whole sidebar in Fira Code, using monospace as decoration
  rather than for data. Monospace now appears only in code.
- No token system: colours and sizes were scattered literals. Everything now
  comes from the CSS variables in `custom.css`.
- Not changed on purpose: no cream/terracotta palette, no near-black page
  with an acid accent, no broadsheet hairline columns, no identical rounded
  cards with soft shadows, no all-caps eyebrow labels, no arrows appended to
  buttons, and no fade-up entrance on every section. The single motion is
  one short cover fade on load, removed under `prefers-reduced-motion`.

## Quality floor

Responsive to mobile, visible keyboard focus, `prefers-reduced-motion`
respected, viewport no longer disables zoom, and real page description in
`index.html`.
