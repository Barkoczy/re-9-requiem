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

Zkopírujte výstupní adresář `natives/` do kořenového adresáře hry:

```bash
cp -r /cesta/k/output/natives "/cesta/ke/hre/RESIDENT EVIL requiem BIOHAZARD requiem/"
```

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
├── build-mod.mjs          # Hlavní build skript
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

## Licence

Tento projekt je neoficiální fan překlad. Veškerá práva k obsahu hry náleží
společnosti Capcom Co., Ltd. Překladové texty jsou poskytovány bez záruky
výhradně pro osobní použití.
