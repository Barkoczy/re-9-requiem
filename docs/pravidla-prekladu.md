# Pravidla překladu

Tento dokument definuje závazná pravidla a konvence pro český překlad
Resident Evil 9: Requiem. Dodržování těchto pravidel zajišťuje konzistenci
a profesionální kvalitu napříč všemi 122 překladovými soubory.

---

## 1. Jazyková pravidla

### 1.1 Spisovnost a registr

- **GUI, tutoriály, popisy předmětů, trofeje**: spisovná čeština, vykání
  (imperativ plurálu: „Dokončete", „Získejte", „Použijte").
- **Dialogy**: přirozená mluvená čeština odpovídající charakteru postavy.
  Povoleny hovorové tvary tam, kde to odpovídá kontextu (např. Leon: „Do prdele!",
  „Kurva...").
- **Herní dokumenty (file.msg)**: formální styl odpovídající typu dokumentu
  (dopisy, výzkumné zprávy, oznámení).

### 1.2 Diakritika

Veškerý český text **musí** obsahovat správnou diakritiku:

- Háčky: č, ď, ě, ň, ř, š, ť, ž
- Čárky: á, é, í, ó, ú, ý
- Kroužek: ů

Chybějící diakritika (např. „Zrusit" místo „Zrušit") je považována za
**kritickou chybu**.

### 1.3 Tykání vs. vykání

Konzistence oslovování je klíčová. Pravidla:

| Vztah | Forma | Příklad |
|-------|-------|---------|
| Leon ↔ Sherry/Grace (ch0600) | tykání | „Máš to?" / „Posílám ti to." |
| Leon ↔ Emily (ch1300) | tykání (laskavé) | „Jsi v pořádku?" |
| Grace → Emily | tykání | „Dokážeš je přečíst?" |
| Emily → Grace | vykání | „Vy jste ta paní od předtím." |
| Victor (ch5100) → Grace | vykání | „Slečno Ashcroft, pojďte dál." |
| Grace → Victor | vykání | „Kdo jste? Proč jste mě unesli?" |
| Victor → Leon | tykání | „Jsi vyšetřovatel, ne?" |
| Leon → Victor | tykání | „Kdy sis naposledy čistil zuby?" |
| ch8000 (Zeno) → Leon | vykání | „Pane Kennedy, ukážete mi..." |
| ch1500 (šéf) → Grace | tykání | „Abys prozkoumala..." |
| Grace → ch1500 (šéf) | vykání | „O kterou jste mě žádal." |
| GUI / systémové texty → hráč | vykání | „Dokončete hlavní příběh." |

### 1.4 Uvozovky

V JSON souborech se používají **výhradně rovné (straight) uvozovky**,
escapované zpětným lomítkem:

```json
"Nebo můžeme zahájit tvoji \\\"léčbu.\\\""
```

**Zakázáno**: české uvozovky „ " / » «, anglické kudrnaté " " / ' '.
Tyto znaky způsobují problémy v herním enginu.

---

## 2. Co se nepřekládá

### 2.1 Jména postav

Všechna jména zůstávají v angličtině:

- Leon S. Kennedy, Grace Ashcroft, Emily, Victor Gideon
- Spencer, Chloe, Sherry, Alyssa, Zeno
- Chris Redfield, Jill Valentine, Albert Wesker (historické zmínky)

### 2.2 Názvy míst

- Raccoon City, R.P.D. (Raccoon Police Department)
- Wrenwood Hotel, Rhodes Hill, ARK
- Spencer Mansion (historické zmínky)

### 2.3 Názvy zbraní a předmětů

Herní názvy zbraní zůstávají v angličtině:

- Matilda IMP, S&S M232, MSBG 500, Requiem
- First Aid Spray, Green Herb, Red Herb
- Mortal Edge, Hunting Knife, R.I.P. Knife, Kotetsu
- Body Armor, Hatchet

### 2.4 Zkratky a organizace

- BSAA, FBI, DSO, S.T.A.R.S., R.P.D.
- Umbrella Corporation (skloňuje se: „Umbrelly", genitiv)
- The Connections (nesklonné)
- T-Virus, Elpis (nesklonné)

### 2.5 Technické značky

Následující značky se zachovávají beze změny:

| Značka | Význam | Příklad |
|--------|--------|---------|
| `<ICON xxx>` | Ikona ovládání | `<ICON INTERACT>` |
| `<REF xxx>` | Odkaz na jiný text | `<REF TutorialList_023_Description>` |
| `<COLOR preset="xxx">` | Barevné zvýraznění | `<COLOR preset="TextColor0">` |
| `<Sound Team ID>` | Zvukový identifikátor | zachovat doslova |
| `\r\n` | Zalomení řádku | zachovat přesně |
| `\n` | Zalomení řádku | zachovat přesně |
| `#Rejected#` | Odmítnutý předmět | zachovat doslova |

---

## 3. Terminologický slovník

Konzistentní překlad klíčových herních termínů:

| Angličtina | Čeština | Poznámka |
|------------|---------|----------|
| Blood Collector | sběrač krve | zařízení Grace |
| Supply Crate | zásobovací bedna | obchod/úložiště |
| Dot Sight | kolimační hledáček | zaměřovač na zbrani |
| Infected blood | nakažená krev | ne „infikovaná" |
| Microsamples | mikrovzorky | měna z krve |
| Crafting | výroba | ne anglicky |
| Save Room | místnost s psacím strojem | bezpečná místnost |
| Typewriter | psací stroj | ukládací bod |
| Ink Ribbon | inkoustová páska | save item |
| Difficulty: Insanity | Šílenství | |
| Difficulty: Standard | Standardní | |
| Difficulty: Casual | Příležitostná | |
| Plant 43 | Plant 43 | nepřekládat |
| Licker | Licker | nepřekládat |
| Zombie | zombík / zombíci | skloňuje se česky |
| Chunk | Chunk | jméno bosse |
| Titan Spinner | Titan Spinner | jméno bosse |
| Tyrant | Tyrant | jméno bosse |
| Mr. Raccoon | Mr. Raccoon | sběratelské figurky |
| Parry / Guard Attack | parírování | obranný útok |
| Finishing move | dokončovací útok | |
| Rhodes Hill Chronic Care Center | pečovatelské centrum Rhodes Hill | |
| Trophy | trofej | achievement |
| Concept art | koncepty | ne „koncepční art" |

---

## 4. Formátování

### 4.1 Zalomení řádků

Herní engine má omezenou šířku textového pole. Při překladu:

- Zachovávejte přibližný počet řádků originálu.
- Používejte `\n` pro zalomení v popisech předmětů.
- Používejte `\r\n` tam, kde ho používá originál (GUI, dokumenty).
- Nedělte slova uprostřed.

### 4.2 Formátovací řetězce

Zachovávejte všechny formátovací zástupné znaky:

- `{0}`, `{1}`, `%d`, `%s` — parametry
- `<ICON xxx>` — herní ikony
- `<REF xxx>` — reference na jiné texty

### 4.3 Prázdné řetězce

Prázdný řetězec `""` znamená, že položka nemá text (zvukový trigger, oddělovač
scény apod.). **Neodstraňujte** je a **nepřidávejte** k nim text.

---

## 5. Kontrola kvality

### 5.1 Automatické kontroly

Před buildem by měly proběhnout:

- Kontrola chybějících klíčů (každý klíč v originálu musí být v překladu)
- Kontrola zachování tagů (`<ICON>`, `<REF>`, `<COLOR>`, `<Sound Team ID>`)
- Kontrola kudrnatých uvozovek (nesmí se vyskytovat)
- Kontrola diakritiky (GUI a systémové texty musí mít diakritiku)
- Kontrola formátovacích řetězců (`{0}`, `%d` musí odpovídat originálu)

### 5.2 Manuální kontroly

- Konzistence tykání/vykání v rámci scén
- Přirozenost českých frází (ne doslovný překlad z angličtiny)
- Správný rod přídavných jmen a zájmen
- Správné pády po předložkách
- Atmosféra odpovídající survival horror žánru

### 5.3 Známé výjimky

- `gui_credits.msg.23` — převážně anglická jména (vývojářský tým), diakritika
  není vyžadována
- `powerupability.msg.23` — originál nemá anglické texty, překlad je prázdný
- `Menu_Renet_Detail0/1` v `gui_menu.msg.23` — právní texty Capcom
  (zásady ochrany soukromí), záměrně nepřeloženy
