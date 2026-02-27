# Repository Guidelines

## Project Structure & Module Organization
- `translations/` contains the authoritative Czech localization as flat JSON maps, mirroring in-game paths (for example `translations/natives/stm/message/dialog/*.json`).
- `json/` holds extracted source data from game assets for comparison; treat it as local reference data.
- `build-mod.mjs` is the main build pipeline that reads original `.msg.23` files, applies Czech strings to the Polish slot, and writes a `natives/` output tree.
- `scripts/extract/` includes extraction utilities (`extract-all.mjs`, `extract.mjs`) for MSG -> JSON workflows.
- `scripts/translate/` contains one-off/batch translation helpers.
- `scripts/utils/` contains maintenance tools (for example `patch-remsg.mjs` and validation scripts).
- `docs/` contains project documentation (Czech).

## Build, Test, and Development Commands
- `npm install` installs dependencies and runs the postinstall patch for `remsg`.
- `npm run patch` reapplies the `remsg` uint64 fix if needed.
- `npm run build` builds localized `.msg.23` files from `translations/`.
- `RE9_GAME_DATA=/path/to/game-data RE9_MOD_OUTPUT=/path/to/output npm run build` overrides default input/output paths.
- `node scripts/extract/extract-all.mjs` extracts original assets (set `RE9_GAME_DATA` first).

## Coding Style & Naming Conventions
- JavaScript uses ESM, 2-space indentation, semicolons, and double quotes.
- Python scripts follow standard 4-space indentation and clear module-level constants.
- Keep translation JSON as `"key": "value"` maps; do not rename or remove keys.
- Preserve engine markup and control sequences exactly (`<ICON ...>`, `<REF ...>`, `<COLOR ...>`, `\n`, `\r\n`).
- Keep filenames aligned with game resource names (for example `dialog_hotel3.msg.23.json`).

## Testing Guidelines
- There is no formal unit-test suite yet; validation is build + content checks.
- A change is acceptable only if `npm run build` completes without errors.
- Run quote/tag sanity checks before PRs, for example:
  - `rg -n '[„“”«»]' translations/`
- If using `scripts/utils/*.py` validators, verify and adjust hardcoded source/destination paths before execution.
- Perform in-game smoke checks for menu text, subtitles, and item descriptions.

## Commit & Pull Request Guidelines
- Use Conventional Commits: `<type>(<scope>): <summary>`.
- Recommended types/scopes: `fix|feat|refactor|docs|chore` with `dialog|gui|gamesystem|sound|build|*`.
- Keep branches focused (`fix/*`, `feat/*`) and diffs small.
- PRs should include: purpose, affected files/areas, verification commands, and representative before/after text examples (plus screenshots when UI readability changed).
