# Architektura projektu

Technický popis formátů, pipeline a nástrojů použitých v českém překladu
Resident Evil 9: Requiem.

---

## 1. RE Engine a formát MSG v23

### 1.1 Přehled

Resident Evil 9 běží na **RE Engine** (Capcom). Herní texty jsou uloženy
v binárním formátu **MSG v23** (`.msg.23`) uvnitř KPKA archivů (`.pak`).

### 1.2 Struktura MSG souboru

Každý MSG soubor obsahuje:

- **Hlavičku** s offsety a metadaty
- **Jazykové sloty** (15 jazyků):

  | Index | Jazyk | Index | Jazyk |
  |-------|-------|-------|-------|
  | 0 | ja (japonština) | 8 | (neznámý) |
  | 1 | en (angličtina) | 9 | pt-br (brazilská portugalština) |
  | 2 | fr (francouzština) | 10 | ko (korejština) |
  | 3 | it (italština) | 11 | zh-tw (tradiční čínština) |
  | 4 | de (němčina) | 12 | zh-cn (zjednodušená čínština) |
  | 5 | es (španělština) | 13 | ar (arabština) |
  | 6 | ru (ruština) | 14 | es-mx (mexická španělština) |
  | 7 | **pl (polština)** | | |

- **Atributy** — metadata k položkám (typ 0: uint64, typ 1: string)
- **Stringové tabulky** — deduplikovaná textová data

### 1.3 Strategie překladu

Český jazyk není mezi 15 sloty. Projekt využívá **polský slot (index 7)**
jako nosič českého textu. Hráč v nastavení zvolí „Polski" a uvidí češtinu.

Toto řešení:
- Nevyžaduje úpravu binárního formátu ani herního kódu
- Funguje s originálním herním enginem bez dalších modů
- Zachovává všechny ostatní jazyky nedotčené

---

## 2. Pipeline

```
Originální .msg.23     Extrakce        Překlad         Build           Deploy
   (binární)      ──────────────►  ──────────────►  ──────────►  ──────────────►
                   extract-all.mjs   (manuální /     build-mod.mjs   cp do hry
                   → json/           AI-asistovaný)  → mod/
                                     → translations/
```

### 2.1 Extrakce (MSG → JSON)

**Skript**: `scripts/extract/extract-all.mjs`

Pomocí knihovny `remsg` dekóduje všechny `.msg.23` soubory ze zdrojového
adresáře (extrahovaný PAK) do čitelných JSON souborů v `json/`.

Výstupní JSON obsahuje kompletní strukturu MSG souboru včetně všech
jazykových slotů, atributů a metadat.

### 2.2 Překlad

**Adresář**: `translations/`

Překladové soubory jsou zjednodušené JSON mapy:

```json
{
  "EntryName_0010_ch0100": "Český překlad textu.",
  "EntryName_0020_ch0200": "Další přeložený text."
}
```

Klíče odpovídají `entry.name` v originálním MSG souboru. Hodnoty jsou
české překlady.

Překlad byl proveden kombinací:
- AI-asistovaného překladu (Claude) s manuální kontrolou
- Hloubkového auditu kvality (diakritika, gramatika, terminologie, konzistence)

### 2.3 Build (JSON → MSG)

**Skript**: `build-mod.mjs`

Pro každý soubor v `translations/`:

1. Načte originální `.msg.23` (binární)
2. Dekóduje pomocí `remsg.decodeMsg()`
3. Pro každou položku nahradí `entry.strings.pl` českým textem
4. Zakóduje zpět pomocí `remsg.encodeMsg()`
5. Zapíše do výstupního adresáře

**Konfigurace** přes environment proměnné:

| Proměnná | Výchozí | Popis |
|----------|---------|-------|
| `RE9_GAME_DATA` | `/mnt/c/Users/henri/Documents/RE-Requiem-CZ` | Cesta k originálním herním datům |
| `RE9_MOD_OUTPUT` | `/mnt/c/Users/henri/Documents/RE-Requiem-CZ/mod` | Výstupní adresář pro mod |

### 2.4 Deploy

Výstupní adresář `mod/natives/` se zkopíruje do kořenového adresáře hry.
Herní engine automaticky načte modifikované `.msg.23` soubory.

---

## 3. Oprava remsg (uint64 bug)

### 3.1 Problém

Knihovna `remsg` v1.2.0 obsahuje bug v `dist/encode.mjs`:

- **Dekódování** čte atributy typu 0 jako `readUint64()` (8 bytů)
- **Enkódování** zapisuje jako `setInt32()` (4 byty)

Sentinel hodnota `0xFFFFFFFFFFFFFFFF` (18446744073709551615) se při enkódování
nevejde do int32 a vyhodí `RangeError`.

### 3.2 Řešení

Patch v `scripts/utils/patch-remsg.mjs` automaticky opraví `encode.mjs`
po instalaci (via `postinstall` hook v `package.json`).

Oprava mění `setInt32(entry.attributes[j])` na:

```js
const v = entry.attributes[j];
if (Number.isSafeInteger(v)) {
    encoder.setInt64(BigInt(v));
} else {
    encoder.setInt64(-1n); // sentinel
}
```

Detaily viz `patches/remsg-encode-uint64.md`.

---

## 4. Struktura překladových souborů

### 4.1 Kategorie

| Adresář | Počet | Obsah |
|---------|-------|-------|
| `dialog/` | 26 | Herní dialogy (cutscény, rádio, reakce) |
| `gui/` | 14 | Uživatelské rozhraní (menu, inventář, mapa, nastavení) |
| `gamesystem/` | 17 | Herní systémy (předměty, úkoly, trofeje, tipy, dokumenty) |
| `soundsupport/` | 45 | Titulky ke zvukovým efektům |
| `importedpackage/dev1term/` | 13 | Systémové texty (GDPR, EULA, nastavení) |
| `develop/` | 3 | Vývojářské soubory |

### 4.2 Pojmenování klíčů

Klíče sledují konvenci RE Enginu:

```
{Prefix}_{SceneID}_{SequenceID}_ch{CharacterID}
```

Příklad: `Hotel3_c111s900_0100_ch5100`
- `Hotel3` — dialog soubor (Hotel, kapitola 3)
- `c111s900` — scéna c111, subscéna 900
- `0100` — pořadí v sekvenci
- `ch5100` — postava (Victor Gideon)

### 4.3 ID postav

| ID | Postava | Role |
|----|---------|------|
| ch0100 | Leon S. Kennedy | Hlavní hrdina (agent DSO) |
| ch0200 | Grace Ashcroft | Hratelná postava (analytička FBI) |
| ch0600 | Sherry Birkin | Leonova partnerka (operátorka) |
| ch0700 | Chloe | Spojenkyně |
| ch1300 | Emily | Dívka zachráněná z hotelu |
| ch1500 | Šéf Grace | Nadřízený Grace ve FBI |
| ch5100 | Victor Gideon | Hlavní antagonista (vědec) |
| ch8000 | Zeno | Tajemná postava |
| ch4000 | NPC / nepřátelé | Různé vedlejší postavy |
| ch4400 | Mutanti | Mutované bytosti (zkomoleniny) |
| dummy | Systémové | Kontextové narativní texty |

---

## 5. Závislosti

| Balíček | Verze | Účel |
|---------|-------|------|
| [remsg](https://www.npmjs.com/package/remsg) | ^1.2.0 | Dekódování/enkódování RE Engine MSG v23 |
| [binary-util](https://www.npmjs.com/package/binary-util) | (transitivní) | Binární čtení/zápis pro remsg |

Projekt nemá žádné další runtime závislosti.
