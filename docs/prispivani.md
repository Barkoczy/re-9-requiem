# Průvodce přispíváním

Návod pro úpravy a rozšiřování českého překladu RE9: Requiem.

---

## 1. Příprava prostředí

### 1.1 Požadavky

- **Node.js** >= 18
- **Git**
- Originální herní data (extrahovaný PAK archiv)
- Textový editor s podporou UTF-8 a JSON (VS Code doporučen)

### 1.2 Klonování a nastavení

```bash
git clone <repo-url>
cd re-9-requiem
npm install
```

`npm install` automaticky nainstaluje `remsg` a aplikuje patch pro uint64 bug.

### 1.3 Extrakce originálních dat

Pokud potřebujete aktuální JSON referenci originálních textů:

```bash
# Nastavte cestu k herním datům
export RE9_GAME_DATA="/cesta/k/extrahovanemu/pak"

# Extrahujte všechny MSG soubory do json/
node scripts/extract/extract-all.mjs
```

---

## 2. Úprava překladů

### 2.1 Formát překladových souborů

Soubory v `translations/` jsou prosté JSON mapy:

```json
{
  "KlíčPoložky": "Český překlad",
  "KlíčPoložky_0010_ch0100": "Dialog postavy Leon."
}
```

### 2.2 Pravidla

Před jakoukoliv úpravou si přečtěte:

- **[Pravidla překladu](pravidla-prekladu.md)** — závazná jazyková a technická
  pravidla

Nejdůležitější body:

1. **Diakritika** — vždy správné háčky a čárky
2. **Tagy** — `<ICON>`, `<REF>`, `<COLOR>`, `<Sound Team ID>` zachovat beze
   změny
3. **Uvozovky** — pouze rovné (`\"` v JSON), nikdy kudrnaté
4. **Klíče** — neměnit, nepřidávat nové, neodstraňovat existující
5. **Prázdné řetězce** — ponechat prázdné (jsou záměrné)

### 2.3 Workflow pro úpravu

1. Otevřete příslušný soubor v `translations/`
2. Najděte klíč, který chcete upravit
3. Pro kontext porovnejte s originálním anglickým textem v `json/` (pokud
   máte extrahovaná data)
4. Upravte český text
5. Spusťte build a otestujte ve hře

### 2.4 Přidání překladu pro nový klíč

Pokud aktualizace hry přidá nové textové klíče:

1. Znovu extrahujte originální data (`node scripts/extract/extract-all.mjs`)
2. Porovnejte klíče v `json/` s klíči v `translations/`
3. Přidejte chybějící klíče s českým překladem
4. Zachovejte pořadí klíčů odpovídající originálu

---

## 3. Build a testování

### 3.1 Build modu

```bash
npm run build
```

Výstup zobrazí počet nahrazených řetězců pro každý soubor:

```
OK: natives/stm/message/dialog/dialog_hotel3.msg.23 (294 strings replaced)
OK: natives/stm/message/gui/gui_common.msg.23 (275 strings replaced)
...
Done! 115 files built, 11451 strings replaced
```

### 3.2 Instalace a testování ve hře

```bash
cp -r "/cesta/k/output/natives" "/cesta/ke/hře/"
```

Ve hře: **Nastavení → Jazyk → Polski**

### 3.3 Kontrolní body při testování

- [ ] Hlavní menu — všechny položky v češtině s diakritikou
- [ ] Nastavení — popisky a hodnoty v češtině
- [ ] Inventář — názvy předmětů anglicky, popisy česky
- [ ] Dialogy — titulky odpovídají kontextu, správné tykání/vykání
- [ ] Dokumenty — čitelné, správná diakritika
- [ ] Trofeje — názvy a popisy konzistentní

---

## 4. Konvence pro commity

### 4.1 Formát commit zprávy

```
<typ>(<oblast>): <stručný popis>

[Volitelné tělo s podrobnostmi]
```

Typy:
- `fix` — oprava překladu (překlep, gramatika, chybějící diakritika)
- `feat` — nový překlad (nový soubor, nové klíče)
- `refactor` — reorganizace bez změny obsahu
- `docs` — dokumentace
- `chore` — build, tooling, CI

Oblasti:
- `dialog` — dialogové soubory
- `gui` — uživatelské rozhraní
- `gamesystem` — herní systémy (předměty, trofeje, tipy...)
- `sound` — zvukové titulky
- `build` — build pipeline
- `*` — více oblastí

### 4.2 Příklady

```
fix(dialog): oprava rodu "zkurvenej vina" → "zkurvená vina"

Tři výskyty v dialog_mangm3 (ch4400 mutant lines).
Mužský tvar přídavného jména u podstatného jména ženského rodu.

fix(gamesystem): oprava překlepu "dloholetému" → "dlouholetému" v file.msg

feat(gui): překlad gui_common — 275 řetězců

chore(build): přechod na ESM a relativní cesty v build-mod.mjs
```

---

## 5. Struktura větví

| Větev | Účel |
|-------|------|
| `main` | Stabilní verze překladu (builditelná a testovaná) |
| `fix/*` | Opravy jednotlivých problémů |
| `feat/*` | Nové překlady nebo rozšíření |

---

## 6. Řešení problémů

### Build selhává s RangeError (uint64)

```
RangeError: The value of "value" is out of range.
It must be >= -2147483648 and <= 2147483647.
```

**Řešení**: Patch remsg nebyl aplikován. Spusťte `npm run patch`.

### Build selhává s "Cannot read properties of null"

Soubor nemá žádné textové položky. Toto je ošetřeno v `build-mod.mjs`
(SKIP), ale pokud se problém objeví, zkontrolujte, že soubor v `translations/`
obsahuje validní JSON.

### Kudrnaté uvozovky v textu

Herní engine nezvládá kudrnaté uvozovky (české „ " ani anglické " ").
Pokud se ve hře zobrazí rozbitý text, zkontrolujte JSON soubor na přítomnost
non-ASCII uvozovek.

Vyhledání:
```bash
grep -rn '[""„"»«]' translations/
```
