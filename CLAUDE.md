# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Czech translation mod for **Resident Evil 9: Requiem** (RE Engine). Replaces the **Polish language slot (index 7)** in `.msg.23` binary files with Czech text — the player selects "Polski" in-game settings to see Czech. Covers ~122 files / ~11,450 strings.

## Build & Commands

```bash
npm install          # Install deps + auto-patch remsg (postinstall hook)
npm run build        # Build mod: apply translations to original MSG files
npm run patch        # Manually re-apply remsg uint64 patch
```

**Required environment variables** (or edit defaults in `build-mod.mjs`):
- `RE9_GAME_DATA` — path to extracted PAK archive with original `.msg.23` files
- `RE9_MOD_OUTPUT` — output directory for the built mod

Node.js >= 18, ESM (`"type": "module"`). Single runtime dependency: `remsg` ^1.2.0.

## Pipeline: Extract → Translate → Build

1. **Extract** (`scripts/extract/extract-all.mjs`): Decode `.msg.23` → JSON via `remsg.decodeMsg()` into `json/` (gitignored). Single-file: `node scripts/extract/extract.mjs <file.msg.23>`.
2. **Translate** (`scripts/translate/*.py`): One-off Python scripts that contain Czech translations as dictionaries and write JSON files to `translations/`. Not part of the build pipeline.
3. **Build** (`build-mod.mjs`): For each JSON in `translations/`, loads the matching original `.msg.23`, decodes it, replaces `entry.strings.pl` with Czech text (matched by `entry.name`), re-encodes, writes to output dir.
4. **Deploy**: Copy `mod/natives/` into the game root directory.

## Translation File Format

Simple JSON maps in `translations/natives/stm/...`:
```json
{
  "EntryName_0010_ch0100": "Český překlad.",
  "EntryName_0020_ch0200": "Další text."
}
```

Keys match `entry.name` in the original MSG file. Empty strings `""` are intentional (sound triggers, scene separators).

## Key Conventions

**Preserve verbatim:** `<ICON>`, `<REF>`, `<COLOR>`, `<Sound Team ID>`, `\r\n`, `\n`, `{0}`, `%d` tags.

**Quotes:** Straight quotes only (`\"` in JSON) — never curly/typographic.

**Czech language rules** (see `docs/pravidla-prekladu.md`):
- GUI/tutorials/descriptions: formal Czech, plural imperative (vykání)
- Dialogs: natural spoken Czech, colloquial forms allowed
- Diacritics mandatory — missing diacritics = critical error
- Character names, place names, weapon names, abbreviations (BSAA, FBI, S.T.A.R.S.) stay in English

**Tykání/vykání matrix** (defined in `docs/pravidla-prekladu.md`): Leon ↔ Sherry/Grace: tykání; Victor ↔ Grace: vykání; system → player: vykání.

## Remsg Patch

`remsg` v1.2.0 has a uint64 encode bug (writes 4 bytes, reads 8). The postinstall hook (`scripts/utils/patch-remsg.mjs`) fixes `encode.mjs` to use `setInt64(BigInt(v))`. Details in `patches/remsg-encode-uint64.md`.

## Validation Tools

- `scripts/utils/verify_translations.py` — checks translation keys match originals (no missing/extra/empty)
- `scripts/utils/final_check.py` — validates JSON, checks HTML/XML tag preservation
- `scripts/utils/fix_quotes.py` — fixes typographic quotes in translation scripts

## Commit Convention

Format: `<type>(<scope>): <description>`
Types: `fix`, `feat`, `refactor`, `docs`, `chore`
Scopes: `dialog`, `gui`, `gamesystem`, `sound`, `build`, `*`

## Branching

- `main` — stable translation release
- `fix/*` — bug fixes
- `feat/*` — new translations or extensions
