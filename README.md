# Resident Evil 9: Requiem — Český překlad

Kompletní český překlad hry **Resident Evil 9: Requiem** (Capcom, RE Engine).
Mod nahrazuje polský jazykový slot českým textem — v nastavení hry stačí zvolit
**„Polski"** pro zobrazení češtiny.

## Rozsah překladu

| Kategorie | Souborů | Řetězců |
|-----------|---------|---------|
| Dialogy | 26 | ~3 100 |
| GUI / Menu | 14 | ~5 200 |
| Herní systémy | 17 | ~3 000 |
| Zvukové titulky | 45 | ~600 |
| Systémové texty | 13 | ~200 |
| Vývoj / Ostatní | 7 | ~50 |
| **Celkem** | **122** | **~11 450** |

## Rychlý start

### Požadavky

- [Node.js](https://nodejs.org/) >= 18
- Originální herní data (extrahovaný PAK archiv se soubory `.msg.23`)

### Instalace

```bash
git clone <repo-url> && cd re-9-requiem
npm install          # nainstaluje remsg + automaticky aplikuje patch
```

### Build modu

```bash
# Výchozí cesty (viz build-mod.mjs)
npm run build

# Vlastní cesty přes env proměnné
RE9_GAME_DATA=/cesta/k/game-data RE9_MOD_OUTPUT=/cesta/k/output npm run build
```

### Instalace do hry

Existují 3 způsoby instalace:

#### A) EXE instalátor (doporučeno)

Stáhněte `RE9-CZ-Preklad-v*-Setup.exe` z [Releases](https://github.com/Barkoczy/re-9-requiem/releases).
Instalátor automaticky detekuje herní adresář ze Steam registru, ověří přítomnost
herních souborů (`re_chunk_*.pak`) a zkopíruje překlad.

#### B) Fluffy Mod Manager

Stáhněte `RE9-CZ-Preklad-v*-FluffyMM.zip` z Releases.
Přetáhněte ZIP do [Fluffy Mod Manageru](https://www.nexusmods.com/site/mods/818)
a aktivujte mod.

#### C) Ruční kopírování

Zkopírujte výstupní adresář `natives/` do kořenového adresáře hry:

```bash
cp -r /cesta/k/output/natives "/cesta/ke/hre/RESIDENT EVIL requiem BIOHAZARD requiem/"
```

#### Po instalaci

Ve hře přejděte do **Nastavení → Jazyk → Polski**.

## Struktura projektu

```
re-9-requiem/
├── translations/          # Přeložené JSON soubory (hlavní obsah repozitáře)
│   └── natives/stm/
│       ├── message/
│       │   ├── dialog/        # 26 dialogových souborů
│       │   ├── gui/           # 14 souborů rozhraní
│       │   ├── gamesystem/    # 17 herních systémů
│       │   └── soundsupport/  # 45 zvukových titulků
│       ├── importedpackage/   # 13 systémových textů
│       └── develop/           # 3 vývojové soubory
├── scripts/
│   ├── translate/         # Python skripty použité k překladu
│   ├── extract/           # Skripty pro extrakci MSG → JSON
│   └── utils/             # Validace, opravy, patch remsg
├── patches/               # Dokumentace oprav závislostí
├── docs/                  # Kompletní dokumentace projektu
├── json/                  # Extrahovaná originální data (v .gitignore)
├── installer/             # Instalační soubory (Inno Setup, CLI, Fluffy MM)
├── build-mod.mjs          # Hlavní build skript
├── build-release.mjs      # Sestavení distribučních balíčků
├── package.json           # NPM konfigurace
└── .gitignore
```

## Technologie

- **RE Engine MSG v23** — binární formát se 15 jazykovými sloty
- **[remsg](https://www.npmjs.com/package/remsg)** — dekódování/enkódování MSG souborů
  (s patchem pro uint64 bug, viz `patches/`)
- **Node.js** — build pipeline (extrakce, aplikace překladů, enkódování)
- **Python** — překladové skripty

## Dokumentace

Kompletní dokumentace je v adresáři [`docs/`](docs/):

- [Pravidla překladu](docs/pravidla-prekladu.md) — konvence, terminologie, styl
- [Architektura](docs/architektura.md) — technický popis formátů a pipeline
- [Průvodce přispíváním](docs/prispivani.md) — jak upravovat a přidávat překlady

## Sestavení distribučních balíčků

```bash
npm run build              # sestav mod
npm run release            # vytvoř distribuční balíčky do dist/
```

Výstup v `dist/`:
- `RE9-CZ-Preklad-v*-FluffyMM.zip` — Fluffy Mod Manager
- `RE9-CZ-Preklad-v*-CLI.zip` — CLI instalátor (bat/ps1)
- `inno/` — vstup pro Inno Setup 6 (kompilace: `ISCC.exe re9-cz-mod.iss` → `.exe`)

## Licence

[MIT](LICENSE) — Překladové texty a nástroje.

Veškerá práva k obsahu hry náleží společnosti Capcom Co., Ltd.
Mod je neoficiální fan překlad pro osobní použití.
