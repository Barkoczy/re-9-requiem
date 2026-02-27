# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-02-27

### Added

- Complete Czech translation covering 122 files (~11,450 strings)
  - 26 dialog files (cutscenes, radio, reactions)
  - 14 GUI/menu files (inventory, map, options, save/load)
  - 17 game system files (items, quests, trophies, tips, tutorials)
  - 45 sound support subtitle files
  - 13 system/term files (EULA, GDPR, options)
  - 7 development/misc files
- Build pipeline (`build-mod.mjs`) for applying translations to original MSG v23 files
- Extraction scripts (`scripts/extract/`) for decoding MSG → JSON
- Translation scripts (`scripts/translate/`) with Czech text dictionaries
- Validation tools (`scripts/utils/`) for verifying translation completeness and tag integrity
- Automatic `remsg` uint64 encode bug patch via postinstall hook
- Project documentation: translation rules, architecture, contribution guide
