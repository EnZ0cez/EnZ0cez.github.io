# Design plan — EnZ0's Homepage

Made with Anthropic's `frontend-design` skill (`.claude/skills/frontend-design/`).
Subject: a Shenzhen University CS student's personal notebook — pattern-mining
papers, course notes and programming notes, kept in Chinese and English.
Audience: classmates, teachers and the author himself, mostly reading long
notes. The page's one job: make long notes easy to read and easy to find.

## v2 — the burgundy field (current)

v1 (below) was correct but too quiet: white page, grey sidebar, burgundy only
as link colour. It read as a cleaned-up default theme, not as a place. The
author's feedback was that it still was not beautiful, so v2 spends the
boldness properly.

The one memorable element: **the SZU burgundy becomes a colour field, not an
accent.** The cover and the sidebar are solid burgundy panels; the reading
column stays light so long notes stay comfortable. Burgundy is Shenzhen
University's colour and was already this site's `themeColor` — enlarging it
is a choice from the subject's own world (a university, its campus, its
litchi-red summers), not a generic dark theme.

Tokens
- SZU burgundy `#7E0725` — cover and sidebar field, headings, links.
- Burgundy deep `#4A0416` — the far end of the cover tint and sidebar depth.
- Litchi red `#D64550` — small highlights only: the active page marker and
  text selection. Named for SZU's litchi (荔园), used sparingly.
- Paper `#FDFCFA` — reading background, near-white, not a cream palette.
- Ink `#262022` — body text.
- Code night `#24181C` — code blocks only, a burgundy-tinted dark, chosen
  because code is read like an editor, not like a page.
- Line `#E7DFDA` — dividers on paper.

Type (unchanged families, bigger scale)
- Display and headings: `Noto Serif SC` 900. The cover title is set at
  `clamp(3rem, 9vw, 5.2rem)` — type itself is the hero treatment.
- Body: `Noto Sans SC`, 17px, line-height 1.8, line length near 72ch.
- Code: `JetBrains Mono` — code only.

Layout
- Cover: the existing stair photo under a burgundy duotone (Docsify's cover
  mask tinted burgundy, deepening downward), round portrait with a paper
  ring, huge serif title in paper white, one ghost button (GitHub) and one
  solid paper button (开始阅读). One orchestrated entrance: portrait,
  title, quote and buttons rise in sequence once on load; removed under
  `prefers-reduced-motion`.
- Sidebar: flat burgundy panel, paper-white app name in serif, section
  names in paper, links at 82% paper, active page on a translucent paper
  pill with a litchi bar. Search box translucent on the same field.
- Reading column: left-aligned, 880px. Page titles in burgundy serif with
  a short thick burgundy rule under them; section headings burgundy;
  links gain a pale burgundy highlight on hover; images get one consistent
  10px radius; the homepage opens with the wide `bg.jpg` banner photo.

Review against the generic defaults
- Not the near-black + acid look: the dark field is a saturated school
  colour at large scale with a photo inside it, and the highlight is
  litchi red from the same warm family, not a neon contrast colour.
- Not cream + terracotta: the reading area is near-white paper and the
  warm colour is burgundy, far darker and cooler than terracotta.
- No SaaS cards, no identical shadows, no gradient washes as decoration —
  the only gradient is the cover photo's burgundy tint deepening toward
  the bottom, which is a photographic treatment of the subject's photo.
- No all-caps eyebrows, no numbered markers, no arrows on buttons, no
  fade-up on every section — the single motion is the cover sequence.

## v1 — tokens only (superseded)

Color: SZU burgundy `#7E0725` as link/heading colour only, burgundy deep
`#5E051B`, ink `#211D1F`, paper `#FFFFFF`, stone `#F4F4F2`, line `#E2DEDB`,
pine `#28544A` for focus. Type and reading layout as in v2 but at a smaller
scale, grey sidebar, plain cover. Kept from v1: the token discipline, the
font choices, monospace for code only, responsive layout, visible focus,
reduced-motion support, and the fixes in `index.html` (lang, description,
viewport zoom, duplicate search placeholder).
