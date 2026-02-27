#!/usr/bin/env python3
"""
Translate RE9 credits file from English to Czech.

- Position entries: translate job titles and character roles to Czech
- Name entries: keep original English (people's names)
- Company entries: keep original English
- Organization entries: keep original English (department/team names)

Output format: flat dict {entry_name: translated_text} matching other translation files.
"""

import json
import sys
from pathlib import Path

SOURCE = Path("/tmp/re9-translate/json/natives/stm/message/gui/gui_credits.msg.23.json")
OUTPUT = Path("/tmp/re9-translate/translations/natives/stm/message/gui/gui_credits.msg.23.json")
CHARANAME = Path("/tmp/re9-translate/translations/natives/stm/message/gamesystem/charaname.msg.23.json")

# ─── Character role translations (matching charaname.msg.23.json) ───

CHARACTER_ROLES = {
    "Leon S. Kennedy": "Leon S. Kennedy",
    "Sherry Birkin": "Sherry Birkin",
    "Victor Gideon": "Victor Gideon",
    "Grace Ashcroft": "Grace Ashcroft",
    "Alyssa Ashcroft": "Alyssa Ashcroft",
    "Nathan Dempsy": "Nathan Dempsy",
    "Harry Reed": "Harry Reed",
    "Norman Cole": "Norman Cole",
    "Emily": "Emily",
    "Chloe": "Chloe",
    "Zeno": "Zeno",
    "Robert Kendo": "Robert Kendo",
    "Marvin Branagh": "Marvin Branagh",
    "Ozwell E. Spencer": "Ozwell E. Spencer",
    "Umber Eyes": "Umber Eyes",
    # Translated role names (from charaname)
    "Hooded Man": "Muz v kapuci",
    "The Girl": "Divka",
    "Commander": "Velitel",
    "Nurse": "Sestra",
    "Injured Doctor": "Zraneny doktor",
    "Hotel Manager": "Hotelovy manazer",
    "Reporter": "Reporter",
    "Operator": "Operator",
    "Radio Broadcast": "Hlaseni",
    "Child": "Dite",
    "Children": "Deti",
    "FBI Agent": "Agent FBI",
    "Newscaster A": "Hlasatel A",
    "Newscaster B": "Hlasatel B",
    "Researcher A": "Vyzkumnik A",
    "Researcher B": "Vyzkumnik B",
    "Researcher C": "Vyzkumnik C",
    "Researcher D": "Vyzkumnik D",
    "Researcher E": "Vyzkumnik E",
    "BSAA Squad Leader": "Velitel druzstva BSAA",
    "BSAA Radio": "Radio BSAA",
    "BSAA Commando A": "Komando BSAA A",
    "BSAA Commando B": "Komando BSAA B",
    "BSAA Commando C": "Komando BSAA C",
    "BSAA Commando D": "Komando BSAA D",
    "BSAA Commando E": "Komando BSAA E",
    "The Connections Soldier": "Vojak The Connections",
    "Chainsaw Doctor": "Doktor s motorovou pilou",
    "Elite Guards": "Elitni straze",
    "Civilians": "Civiliste",
    "Zombies": "Zombie",
    "Stunts": "Kaskaderi",
    "Motion Actors": "Pohyboví herci",
    "Motion Capture Actors": "Herci pro snimani pohybu",
}

# ─── Complete position translation map (all 513 unique entries) ───

POSITION_TRANSLATIONS = {
    # ── Job titles ──
    "Director": "Reziser",
    "Producer": "Producent",
    "Executive Producer": "Vykonny producent",
    "Associate Producer": "Asociovany producent",
    "Line Producer": "Liniovy producent",
    "Mocap Producer": "Producent mocapu",
    "Score Producer": "Producent hudby",
    "Creative Director": "Kreativni reziser",
    "Art Director": "Umelecky reziser",
    "Audio Director": "Zvukovy reziser",
    "Music Director / Lead Composer": "Hudebi reziser / Hlavni skladatel",
    "Presentation Director": "Prezentacni reziser",
    "Production Director": "Produkci reziser",
    "Technical Director": "Technicky reziser",
    "Senior Technical Director": "Starsi technicky reziser",
    "Program Director": "Programovy reziser",
    "Test Director": "Reziser testovani",
    "Director Manager": "Reziser a manazer",
    "Level & Environment Director": "Reziser urovni a prostredi",
    "Agency Director": "Reziser agentury",
    "Localization Director": "Reziser lokalizace",
    "Director of Localization": "Reziser lokalizace",
    "Director of QA": "Reziser zajisteni kvality",
    "Director of Client Partnerships": "Reziser klientskych partnerstvi",
    "Commercial Director": "Komercni reziser",
    "Marketing Director": "Marketingovy reziser",
    "Sales & Marketing Director": "Reziser prodeje a marketingu",
    "Managing Director": "Generalni reditel",
    "Enterprise Sales Director": "Reziser podnikoveho prodeje",
    "Director, Business Administration": "Reziser obchodni spravy",
    "Director, Client Engagement": "Reziser klientske spoluprace",
    "Director, Digital Sales": "Reziser digitalniho prodeje",
    "Director, LATAM Digital Sales & Marketing": "Reziser dig. prodeje a marketingu LATAM",
    "Director, Licensing": "Reziser licencovani",
    "Director, Marketing": "Reziser marketingu",
    "Director, Voice Over Services": "Reziser dabingovych sluzeb",

    "General Manager": "Generalni manazer",
    "Manager": "Manazer",
    "Engineering Manager": "Manazer inzenyrstvi",
    "Cinematic Manager": "Manazer cinematik",
    "Rendering Manager": "Manazer renderovani",
    "Production Manager": "Produkci manazer",
    "Production Managers": "Produkci manazeri",
    "Post Production Manager": "Manazer postprodukce",
    "Senior Production Manager": "Starsi produkci manazer",
    "Senior Production Coordinator": "Starsi produkci koordinator",
    "Operation Manager": "Provozni manazer",
    "Operations Manager": "Provozni manazer",
    "Facility Manager": "Manazer zarizeni",
    "Security Manager": "Bezpecnostni manazer",
    "Legal Manager": "Pravni manazer",
    "Brand Manager": "Manazer znacky",
    "Marketing Manager": "Marketingovy manazer",
    "Senior Marketing Manager": "Starsi marketingovy manazer",
    "PR & Marketing Manager": "Manazer PR a marketingu",
    "PR Manager Central Europe": "Manazer PR pro stredni Evropu",
    "Senior PR Manager": "Starsi manazer PR",
    "Community Manager": "Manazer komunity",
    "Community Manager, Polish-speaking Communities": "Manazer komunity, polsky mluvici komunity",
    "Business Development Manager": "Manazer obchodniho rozvoje",
    "Business Operations Manager": "Manazer obchodnich operaci",
    "Business Operations Administrator": "Administrator obchodnich operaci",
    "Business Services Administrator": "Administrator obchodnich sluzeb",
    "Digital Sales Account Manager": "Manazer uctu digitalniho prodeje",
    "Associate Marketing Services Manager": "Asociovany manazer marketingovych sluzeb",
    "Associate PR & Events Manager": "Asociovany manazer PR a akci",
    "Senior Business Support Manager": "Starsi manazer obchodni podpory",
    "Sales and Licensing Manager EMEA": "Manazer prodeje a licencovani EMEA",
    "Senior Sales & Marketing Manager": "Starsi manazer prodeje a marketingu",
    "Senior Marketing Services Manager": "Starsi manazer marketingovych sluzeb",

    "Senior Manager": "Starsi manazer",
    "Senior Managers": "Starsi manazeri",
    "Senior Manager, Brand Marketing": "Starsi manazer znackoveho marketingu",
    "Senior Manager, Business Development": "Starsi manazer obchodniho rozvoje",
    "Senior Manager, Business Strategy": "Starsi manazer obchodni strategie",
    "Senior Manager, Digital Accounts": "Starsi manazer digitalnich uctu",
    "Senior Manager, Events": "Starsi manazer akci",
    "Senior Manager, Licensing": "Starsi manazer licencovani",
    "Senior Manager, Licensing Operations": "Starsi manazer licencnich operaci",
    "Senior Manager, Marketing Strategy": "Starsi manazer marketingove strategie",
    "Senior Manager, Sales Administration": "Starsi manazer obchodni administrativy",
    "Senior Manager, Social Media & Community": "Starsi manazer socialnich siti a komunity",
    "Assistant Senior Manager": "Asistent starsiho manazera",

    "Associate Manager, Social Media and Community": "Asociovany manazer soc. siti a komunity",
    "Associate Director, PR": "Asociovany reziser PR",

    "Senior Director, Business Operations": "Starsi reziser obchodnich operaci",
    "Senior Director, Communications": "Starsi reziser komunikace",
    "Senior Director, Creative Services & Events": "Starsi reziser kreativnich sluzeb a akci",
    "Senior Director, National Sales": "Starsi reziser narodniho prodeje",

    "Senior Vice President": "Starsi viceprezident",
    "Senior Vice President, Digital Platforms": "Starsi viceprezident digitalnich platforem",
    "Vice President, Project Management & Divisional Communications": "Viceprezident projektoveho rizeni a komunikace",
    "Vice President, Sales": "Viceprezident prodeje",

    "CEO": "CEO",
    "CEO / Consultant": "CEO / Konzultant",
    "CEO EA": "CEO EA",
    "COO": "COO",
    "CTO": "CTO",
    "Chief Executive Officer": "Generalni reditel",
    "Chief Operating Officer": "Provozni reditel",

    "Head of Advanced Game Development": "Vedouci pokrocileho vyvoje her",
    "Head of Audio Localization": "Vedouci zvukove lokalizace",
    "Head of Business Services": "Vedouci obchodnich sluzeb",
    "Head of Insight & Research": "Vedouci analyzy a vyzkumu",
    "Head of Physical Production / Capture AD": "Vedouci fyzicke produkce / AD zachycovani",
    "Head of Post Production": "Vedouci postprodukce",
    "Head of Production": "Vedouci produkce",
    "Head of Studio": "Vedouci studia",
    "Head of Technology": "Vedouci technologii",
    "Head of Virtual Production": "Vedouci virtualni produkce",
    "Site Head": "Vedouci pobocky",
    "Studio Head - Los Angeles": "Vedouci studia - Los Angeles",

    # ── Leads ──
    "Lead Animator": "Vedouci animator",
    "Lead Application Programmer": "Vedouci aplikacni programator",
    "Lead Application Programmers": "Vedouci aplikacni programatori",
    "Lead Audio Programmer / Technical Designer": "Vedouci zvukovy programator / Technicky designer",
    "Lead Battle Designer": "Vedouci designer boju",
    "Lead Character Artist": "Vedouci umelec postav",
    "Lead Cinematic Artist": "Vedouci cinematicky umelec",
    "Lead Cinematic Lighting Artist": "Vedouci umelec cinematickeho osvetleni",
    "Lead Concept Artists": "Vedouci konceptualni umelci",
    "Lead Environment Artist": "Vedouci umelec prostredi",
    "Lead Facial Animator": "Vedouci oblicobjovy animator",
    "Lead Facial Animators": "Vedouci oblicejovi animatori",
    "Lead Game Designer": "Vedouci herniho designu",
    "Lead Game Designers": "Vedouci hernich designu",
    "Lead Gimmick Artist": "Vedouci gimmick umelec",
    "Lead Level Designer": "Vedouci designer urovni",
    "Lead Lighting Artist": "Vedouci umelec osvetleni",
    "Lead Motion Capture Tracker": "Vedouci tracker snimani pohybu",
    "Lead Motion Editor": "Vedouci editor pohybu",
    "Lead Project Manager": "Vedouci projektovy manazer",
    "Lead Recordist & Project Manager": "Vedouci nahravac a projektovy manazer",
    "Lead Rigging Artist": "Vedouci rigging umelec",
    "Lead Software Engineer": "Vedouci softwarovy inzenyr",
    "Lead Sound Designer": "Vedouci zvukovy designer",
    "Lead Sound Designers": "Vedouci zvukovi designeri",
    "Lead UI Artist": "Vedouci UI umelec",
    "Lead VFX Artist": "Vedouci VFX umelec",
    "Lead Voice Director": "Vedouci dabingovy reziser",

    # ── Senior roles ──
    "Senior Animator": "Starsi animator",
    "Senior Art Directors": "Starsi umelecti reziseri",
    "Senior Audio Engineer": "Starsi zvukovy inzenyr",
    "Senior Business Analyst": "Starsi obchodni analytik",
    "Senior Communications Manager": "Starsi manazer komunikace",
    "Senior Designer, Graphic Design": "Starsi designer grafickeho designu",
    "Senior Producer / Head of Casting": "Starsi producent / Vedouci castingu",
    "Senior Project Manager": "Starsi projektovy manazer",
    "Senior Project Manager, Creative services": "Starsi projektovy manazer kreativnich sluzeb",
    "Senior Sound Designer": "Starsi zvukovy designer",
    "Senior Specialist, Operations Support": "Starsi specialista provozni podpory",
    "Senior Support Representative, Sales Administration": "Starsi zastupce podpory obchodni administrativy",
    "Senior Test Lead": "Starsi vedouci testovani",
    "Senior Test Manager": "Starsi manazer testovani",
    "Senior Motion Capture Stage TD": "Starsi TD sceny snimani pohybu",
    "Senior Motion Capture Tracker": "Starsi tracker snimani pohybu",
    "Senior Analyst, Data Analytics": "Starsi analytik datove analytiky",

    # ── Programmers ──
    "AI Programmers": "AI programatori",
    "AI Researcher": "AI vyzkumnik",
    "Animation Programmers": "Programatori animaci",
    "Application Programmer": "Aplikacni programator",
    "Application Programmers": "Aplikacni programatori",
    "Audio Programmers": "Zvukovi programatori",
    "Cinematics Programmers": "Programatori cinematik",
    "DCC Tool Programmers": "Programatori DCC nastroju",
    "Network Programmers": "Sitovi programatori",
    "Physics Programmers": "Programatori fyziky",
    "RE ENGINE LIBRARY Programmers": "Programatori knihoven RE ENGINE",
    "Rendering Programmers": "Programatori renderovani",
    "Sound Tool Programmers": "Programatori zvukovych nastroju",
    "Systems & Platforms Programmers": "Programatori systemu a platforem",
    "Tool & Workflow Programmers": "Programatori nastroju a workflow",
    "Tools Programmer": "Programator nastroju",
    "UI Programmers": "UI programatori",
    "VFX Programmers": "VFX programatori",

    # ── Engineers ──
    "Engineers": "Inzenyri",
    "Software Engineer": "Softwarovy inzenyr",
    "Software Engineers": "Softwari inzenyri",
    "Main Software Engineer": "Hlavni softwarovy inzenyr",
    "Main Software Engineers": "Hlavni softwari inzenyri",
    "Security Engineers": "Bezpecnostni inzenyri",
    "Data Engineers": "Datovi inzenyri",
    "Audio Engineer": "Zvukovy inzenyr",
    "Audio Engineers": "Zvukovi inzenyri",
    "Assistant Engineers": "Asistenti inzenyru",
    "Recording Engineers": "Nahravaci inzenyri",
    "Recording & Mixing Engineer": "Nahravaci a mixovaci inzenyr",
    "Foley Studio Engineer": "Inzenyr foley studia",
    "Foley Recording Engineer": "Nahravaci inzenyr foley",
    "VProd Software Engineer": "Softwarovy inzenyr VProd",
    "Solutions Architect": "Architekt reseni",

    # ── Artists ──
    "Artists": "Umelci",
    "3D Artists": "3D umelci",
    "Character Artists": "Umelci postav",
    "Cinematic Artists": "Cinematicti umelci",
    "Concept Artist": "Konceptualni umelec",
    "Concept Artists": "Konceptualni umelci",
    "Environment Artists": "Umelci prostredi",
    "Gimmick Artists": "Gimmick umelci",
    "Lighting Artists": "Umelci osvetleni",
    "Rigging Artists": "Rigging umelci",
    "Simulation VFX Artists": "Simulacni VFX umelci",
    "Technical Artists": "Technicti umelci",
    "UI Artist": "UI umelec",
    "UI Artists": "UI umelci",
    "VFX Artists": "VFX umelci",
    "Make-up Artists": "Vizaziste",
    "Hair & Make-up Artist": "Umelec vlasu a make-upu",

    # ── Animators ──
    "Animators": "Animatori",
    "Facial Animators": "Oblicejovi animatori",
    "Animation Leaders": "Vedouci animaci",
    "Art Leaders": "Vedouci umelci",
    "Assist Animation Leaders": "Pomocni vedouci animaci",

    # ── Designers ──
    "Game Designer": "Hernie designer",
    "Game Designers": "Hernie designeri",
    "Level Designers": "Designeri urovni",
    "Graphic Designers": "Graficti designeri",
    "Tool & UX Designers": "Designeri nastroju a UX",
    "Sound Designer": "Zvukovy designer",
    "Sound Designers": "Zvukovi designeri",

    # ── QA / Testing ──
    "Testers": "Testeri",
    "Quality Assurance": "Zajisteni kvality",
    "QA Lead Testers": "Vedouci QA testeri",
    "QA Managers": "QA manazeri",
    "QA Support": "QA podpora",
    "Standard QA Testers": "Standardni QA testeri",
    "Advanced QA Testers": "Pokrocili QA testeri",

    # ── Sound / Audio ──
    "Cinematic Sound Designers": "Cinematicti zvukovi designeri",
    "Sound Editors": "Zvukovi editori",
    "Sound Effects Editors": "Editori zvukovych efektu",
    "Audio Editors": "Zvukovi editori",
    "Game Audio Mixer": "Zvukovy mixer hry",
    "Mixer": "Mixer",
    "Score Mixer": "Mixer hudby",
    "Foley": "Foley",
    "Foley Artist / Foley Editor": "Foley umelec / Foley editor",
    "Foley Artists": "Foley umelci",
    "Foley Mixer": "Foley mixer",
    "Sound Studio Coordinator": "Koordinator zvukoveho studia",

    # ── Composers ──
    "Composer": "Skladatel",
    "Composers": "Skladatele",
    "Writer": "Scenarista",
    "Dialogue & Text Writers": "Scenariste dialogu a textu",

    # ── Production staff ──
    "Production Assistants": "Produkci asistenti",
    "Production Coordinators": "Produkci koordinatori",
    "Production Runners": "Produkci runners",
    "Post Production Assistants": "Asistenti postprodukce",
    "Post Production Coordinators": "Koordinatori postprodukce",
    "Junior Post Production Coordinators": "Mladsi koordinatori postprodukce",
    "Project Manager": "Projektovy manazer",
    "Project Managers": "Projektoví manazeri",
    "Project Assistant": "Projektovy asistent",
    "Project Manager, Product Operations": "Projektovy manazer produktovych operaci",
    "Project Manager, Project Management & Divisional Communications": "Projektovy manazer PM a komunikace",
    "Release Managers": "Manazeri releaseu",
    "Interim Project Managers": "Docasni projektoví manazeri",
    "Localization Coordinator": "Koordinator lokalizace",
    "Localization Group Managers": "Manazeri skupin lokalizace",
    "Localization Project Managers": "Projektoví manazeri lokalizace",
    "Localization Support": "Podpora lokalizace",
    "Junior Localization Coordinator": "Mladsi koordinator lokalizace",
    "Coordinator, LATAM Communications & Localization": "Koordinator komunikace a lokalizace LATAM",
    "Manager, LATAM Communications & Localization": "Manazer komunikace a lokalizace LATAM",
    "Manager, LATAM Marketing": "Manazer marketingu LATAM",
    "Manager, Analytics & Insights": "Manazer analytiky a analyzy",
    "Manager, Licensing & Business Development": "Manazer licencovani a obchodniho rozvoje",
    "Manager, Operations & Facility": "Manazer provozu a zarizeni",
    "Manager, PR": "Manazer PR",
    "Analyst, Insight & Research": "Analytik analyzy a vyzkumu",
    "Junior Analyst, Emerging Markets": "Mladsi analytik rozvijejicich se trhu",
    "Junior Manager, Sales & Operations": "Mladsi manazer prodeje a provozu",
    "Associate, Business Strategy": "Asociovany analytik obchodni strategie",

    # ── Motion Capture ──
    "Motion Capture Manager": "Manazer snimani pohybu",
    "Motion Capture Supervisor": "Supervizor snimani pohybu",
    "Motion Capture Operators": "Operatori snimani pohybu",
    "Motion Capture Trackers": "Trackeri snimani pohybu",
    "Motion Capture Editors": "Editori snimani pohybu",
    "Motion Capture Stage Assistant": "Asistent sceny snimani pohybu",
    "Motion Capture Stage TD": "TD sceny snimani pohybu",
    "Motion Capture TD": "TD snimani pohybu",
    "Motion Editors": "Editori pohybu",
    "Junior Motion Capture Trackers": "Mladsi trackeri snimani pohybu",
    "Junior Motion Editor": "Mladsi editor pohybu",
    "Facial Capture Operator": "Operator zachyceni obliceje",
    "Assistant Facial Capture": "Asistent zachyceni obliceje",
    "Shogun Operator / Junior Motion Capture Tracker": "Shogun operator / Mladsi tracker snimani pohybu",
    "Shogun Operator / Motion Capture Tracker": "Shogun operator / Tracker snimani pohybu",
    "Reference Camera Operators": "Operatori referencnich kamer",
    "Character Supervisor": "Supervizor postav",
    "3D Scan Models": "3D skenovaci modely",
    "Modeling Agencies": "Modelingove agentury",
    "Digital Continuity": "Digitalni kontinuita",
    "Digital Continuity Assistant": "Asistent digitalni kontinuity",

    # ── Technical ──
    "Technical Art Director": "Technicky umelecky reziser",
    "Technical Architect": "Technicky architekt",
    "Technical Assistant": "Technicky asistent",
    "Technical Managers": "Technicti manazeri",
    "Technical Support": "Technicka podpora",
    "Technical Supervisor / Facial Capture Lead": "Technicky supervizor / Vedouci zachyceni obliceje",
    "Rigging Technical Artist": "Technicky umelec riggingu",
    "Rigging Technical Director": "Technicky reziser riggingu",
    "DCC Tool Manager": "Manazer DCC nastroju",
    "IT Technician": "IT technik",
    "VProd Technician": "VProd technik",
    "Asset Technician": "Technik assetu",
    "Systems Administrator": "Systemovy administrator",
    "Studio Administrator": "Administrator studia",
    "Studio Assistant": "Asistent studia",
    "Solutions Developers": "Vyvojari reseni",
    "Data Analysts": "Datovi analytici",
    "VFX Dev": "VFX vyvojar",
    "VFX Technical Artist": "Technicky VFX umelec",

    # ── Recording / Cinematic ──
    "Recording Directors": "Nahravaci reziseri",
    "Recording Coordinators": "Koordinatori nahravani",
    "Recording Studio": "Nahravaci studio",
    "Recording Studio Coordinators": "Koordinatori nahravaciho studia",
    "Recordists": "Nahravaci",
    "Cinematic Coordinator": "Koordinator cinematik",
    "Cinematic Performance Director / Lead Voice Director / Casting Director": "Reziser cinematickeho herectvi / Vedouci dabingovy reziser / Casting reziser",
    "Voice Director": "Dabingovy reziser",
    "Voice Directors": "Dabingovi reziseri",
    "Casting Director / Motion Actor": "Casting reziser / Pohybovy herec",
    "Casting by": "Casting",
    "Casting & Costume General Manager": "Generalni manazer castingu a kostymu",
    "Casting & Costume Manager": "Manazer castingu a kostymu",
    "Stunt Coordinator": "Koordinator kaskaderu",
    "Stylist": "Stylista",
    "Dialogue Editor": "Editor dialogu",

    # ── Music credits ──
    "Arranged by": "Aranzoval",
    "Composed by": "Slozil",
    "Lyrics by": "Text napsal",
    "Mixed at": "Mixovano v",
    "Mixed by": "Mixoval",
    "Music by": "Hudba",
    "Performed by": "Interpretoval",
    "Produced by": "Produkoval",
    "Vocal Recorded at": "Vokal nahran v",
    "Vocal Recorded by": "Vokal nahral",

    # ── Localization teams by language ──
    "Arabic Editor": "Arabsky editor",
    "Arabic Localization": "Arabska lokalizace",
    "Arabic Testers": "Arabsti testeri",
    "Arabic Translators": "Arabsti prekladatele",
    "Brazilian Portuguese Localization": "Brazilska portugalskas lokalizace",
    "Brazilian Portuguese Support": "Podpora brazilske portugalstiny",
    "Brazilian Portuguese Testers": "Testeri brazilske portugalstiny",
    "English Editor": "Anglicky editor",
    "English Localization": "Anglicka lokalizace",
    "English Senior Tester": "Starsi anglicky tester",
    "English Support": "Anglicka podpora",
    "English Tester": "Anglicky tester",
    "French Editor": "Francouzsky editor",
    "French Localization": "Francouzska lokalizace",
    "French Support": "Francouzska podpora",
    "French Testers": "Francouzsti testeri",
    "French Translators": "Francouzsti prekladatele",
    "German Editor": "Nemecky editor",
    "German Localization": "Nemecka lokalizace",
    "German Senior Tester": "Starsi nemecky tester",
    "German Tester": "Nemecky tester",
    "German Translators": "Nemecti prekladatele",
    "Italian Editor": "Italsky editor",
    "Italian Localization": "Italska lokalizace",
    "Italian Senior Tester": "Starsi italsky tester",
    "Italian Support": "Italska podpora",
    "Italian Tester": "Italsky tester",
    "Italian Translators": "Italsti prekladatele",
    "Japanese Translators": "Japonsti prekladatele",
    "Korean Editor": "Korejsky editor",
    "Korean Localization": "Korejska lokalizace",
    "Korean Support": "Korejska podpora",
    "Korean Testers": "Korejsti testeri",
    "Korean Translators": "Korejsti prekladatele",
    "Latin American Spanish Localization": "Latinskoamericka spanelska lokalizace",
    "Latin American Spanish Support": "Podpora latinskoamericke spanelstiny",
    "Latin American Spanish Testers": "Testeri latinskoamericke spanelstiny",
    "Polish Editor": "Polsky editor",
    "Polish Testers": "Polsti testeri",
    "Polish Translators": "Polsti prekladatele",
    "PortugueseBR Editor": "Portugalsky (BR) editor",
    "PortugueseBR Translators": "Portugalsti (BR) prekladatele",
    "Russian Editor": "Rusky editor",
    "Russian Localization": "Ruska lokalizace",
    "Russian Senior Tester": "Starsi rusky tester",
    "Russian Tester": "Rusky tester",
    "Russian Translators": "Rusti prekladatele",
    "Simplified Chinese Linguists": "Lingviste zjednodusene cinstiny",
    "Simplified Chinese Localization": "Lokalizace zjednodusene cinstiny",
    "Simplified Chinese Support": "Podpora zjednodusene cinstiny",
    "Simplified Chinese Testers": "Testeri zjednodusene cinstiny",
    "Spanish Localization": "Spanelska lokalizace",
    "Spanish Support": "Spanelska podpora",
    "Spanish Testers": "Spanelsti testeri",
    "SpanishES Editor": "Spanelsky (ES) editor",
    "SpanishES Translators": "Spanelsti (ES) prekladatele",
    "SpanishMX Editor": "Spanelsky (MX) editor",
    "SpanishMX Translators": "Spanelsti (MX) prekladatele",
    "Traditional Chinese Linguists": "Lingviste tradicni cinstiny",
    "Traditional Chinese Localization": "Lokalizace tradicni cinstiny",
    "Traditional Chinese Support": "Podpora tradicni cinstiny",
    "Traditional Chinese Testers": "Testeri tradicni cinstiny",
    "Translators": "Prekladatele",
    "Assistant Localization Directors": "Pomocni reziseri lokalizace",

    # ── Sales / Marketing / PR / Events ──
    "Marketing Dept. / Director": "Marketingove odd. / Reziser",
    "Marketing Dept. / Manager": "Marketingove odd. / Manazer",
    "Marketing Dept. / Specialists": "Marketingove odd. / Specialiste",
    "Marketing Assistant": "Marketingovy asistent",
    "Marketing Executive": "Marketingovy reditel",
    "Marketing Supervisor": "Marketingovy supervizor",
    "Sales Executive": "Obchodni reditel",
    "Sales Supervisor": "Obchodni supervizor",
    "Sales & Marketing Executives": "Reditele prodeje a marketingu",
    "Events & Marketing Coordinator": "Koordinator akci a marketingu",
    "Event & Marketing Coordinator France": "Koordinator akci a marketingu Francie",
    "Social Media and Community Manager - Italy": "Manazer soc. siti a komunity - Italie",
    "Social Media and Community Manager - MENA": "Manazer soc. siti a komunity - MENA",
    "Social Media and Community Manager - Spain": "Manazer soc. siti a komunity - Spanelsko",
    "Specialist, Digital Sales": "Specialista digitalniho prodeje",
    "Specialist, Social Media & Customer Support": "Specialista soc. siti a zakaznicke podpory",
    "Licensing & Esports Liaison": "Spojka licencovani a esportu",
    "Licensing Coordinator": "Koordinator licencovani",
    "Operations Assistants": "Provozni asistenti",
    "Operations Coordinator": "Provozni koordinator",
    "Country Manager GSA / Digital Commercial Director EMEA": "Krajsky manazer GSA / Digitalni komercni reziser EMEA",

    # ── Legal / IP / Data ──
    "Copyright Team": "Tym autorskych prav",
    "Data Privacy Team": "Tym ochrany dat",
    "Patent Team": "Patentovy tym",
    "Review Team": "Recenzni tym",
    "Script Review": "Recenze scenare",
    "Trademark & Copyright Section": "Sekce ochrannych znamek a autorskych prav",
    "Trademark Team": "Tym ochrannych znamek",
    "Tuning Team": "Ladicí tym",
    "Vendor Managers": "Manazeri dodavatelu",

    # ── Special Thanks ──
    "Special Thanks": "Specialni podekovani",
    "Special Thanks\uff1aMonotype Imaging Inc.": "Specialni podekovani: Monotype Imaging Inc.",
    "Special Thanks\uff1aYOONDESIGN GROUP INC.": "Specialni podekovani: YOONDESIGN GROUP INC.",

    # ── Legal / special text in Position fields ──
    "Leon's brown sheepskin leather bomber jacket appears with permission from Schott NYC.":
        "Leonova hneda kozena bombr bunda z ovci kuze se objevuje se svolenim Schott NYC.",
    "Leon\u2019s brown sheepskin leather bomber jacket appears with permission from Schott NYC.":
        "Leonova hneda kozena bombr bunda z ovci kuze se objevuje se svolenim Schott NYC.",
    "The\xa0typefaces\xa0included\xa0herein\xa0are\xa0solely\xa0developed\xa0by\xa0DynaComware.":
        "Pismena obsazena v tomto dile byla vyvinuta vyhradne spolecnosti DynaComware.",
    "ZWrap (Copyright \u00a9 2023 Faceform LLC).":
        "ZWrap (Copyright \u00a9 2023 Faceform LLC).",
    "Facial Animation Technology provided by Faceware Technologies":
        "Technologie oblicejove animace poskytnuta spolecnosti Faceware Technologies",
    "Visual Effects Stock Footage provided by FX Elements.":
        "Videomateriál vizualnich efektu poskytla spolecnost FX Elements.",
    "Visual FX Stock Footage provided by Final Light Productions":
        "Videomaterial vizualnich efektu poskytla spolecnost Final Light Productions",
    "Artbeats Digital Film Library":
        "Artbeats Digital Film Library",
    "Getty Images":
        "Getty Images",
    "Toho Studio Coordinate":
        "Koordinace studia Toho",

    "Zombies, Workers, Civilians, and other Supporting Roles played by:":
        "Zombie, delnici, civiliste a dalsi vedlejsi role hrali:",

    # ── Character roles (from game, matching charaname translations) ──
    **CHARACTER_ROLES,

    # ── Compound character roles ──
    "Emily / Chloe": "Emily / Chloe",
    "BSAA Commando D / Operator": "Komando BSAA D / Operator",
    "BSAA Squad Leader / Zeno Body Double": "Velitel druzstva BSAA / Zenonuv dvojnik",
    "Chainsaw Doctor / Injured Doctor": "Doktor s motorovou pilou / Zraneny doktor",
    "The Connections Soldier / Chainsaw Doctor": "Vojak The Connections / Doktor s motorovou pilou",
    "FBI Agent / Civilian": "Agent FBI / Civilista",
    "Researcher A / Newscaster A": "Vyzkumnik A / Hlasatel A",
    "Researcher C / Newscaster B": "Vyzkumnik C / Hlasatel B",

    # ── Stunt roles ──
    "Stunts: BSAA Commando C": "Kaskaderi: Komando BSAA C",
    "Stunts: BSAA Commando E": "Kaskaderi: Komando BSAA E",
    "Stunts: Commander": "Kaskaderi: Velitel",
    "Stunts: Grace": "Kaskaderi: Grace",
    "Stunts: Leon": "Kaskaderi: Leon",
    "Stunts: Leon, BSAA Commando D": "Kaskaderi: Leon, Komando BSAA D",
    "Stunts: Tyrant": "Kaskaderi: Tyrant",
    "Stunts: Victor, Zeno": "Kaskaderi: Victor, Zeno",

    # ── Other roles ──
    "Advisor": "Poradce",
    "Announcement": "Hlaseni",
    "Announcements": "Hlaseni",

    # ── SE Recording ──
    "SE Recording Support": "Podpora nahravani zvukovych efektu",
}


def translate_entry(entry: dict) -> str:
    """Return the translated text for a credits entry."""
    name = entry["name"]
    en_text = entry["strings"].get("en", "")

    # Name entries: keep original English (people's names)
    if "_Name_" in name or name.startswith("Gui_Credits_Name"):
        return en_text

    # Company entries: keep original English
    if "_Company_" in name or name.startswith("Gui_Credits_Company"):
        return en_text

    # Organization entries: keep original English (department/team names)
    if "_Organization_" in name or name.startswith("Gui_Credits_Organization"):
        return en_text

    # Position entries: translate
    if "_Position_" in name or name.startswith("Gui_Credits_Position"):
        if en_text in POSITION_TRANSLATIONS:
            return POSITION_TRANSLATIONS[en_text]
        else:
            # Fallback: return English with a note for review
            print(f"WARNING: No translation for position: {en_text!r} (entry: {name})",
                  file=sys.stderr)
            return en_text

    # Any other entry type: translate if we have a mapping, otherwise keep
    if en_text in POSITION_TRANSLATIONS:
        return POSITION_TRANSLATIONS[en_text]
    return en_text


def main():
    # Load source
    with open(SOURCE, encoding="utf-8") as f:
        data = json.load(f)

    entries = data["entries"]
    print(f"Total entries: {len(entries)}")

    # Build output dict
    output = {}
    missing_count = 0

    for entry in entries:
        entry_name = entry["name"]
        translated = translate_entry(entry)
        output[entry_name] = translated

    print(f"Output entries: {len(output)}")

    # Ensure output directory exists
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    # Write output
    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"Written to: {OUTPUT}")

    # Summary stats
    positions = [e for e in entries if "Position" in e["name"]]
    names = [e for e in entries if "Name" in e["name"]]
    companies = [e for e in entries if "Company" in e["name"]]
    orgs = [e for e in entries if "Organization" in e["name"]]

    translated_positions = sum(
        1 for e in positions
        if e["strings"].get("en", "") in POSITION_TRANSLATIONS
    )

    print(f"\nBreakdown:")
    print(f"  Positions: {len(positions)} (translated: {translated_positions}, "
          f"missing: {len(positions) - translated_positions})")
    print(f"  Names: {len(names)} (kept as-is)")
    print(f"  Companies: {len(companies)} (kept as-is)")
    print(f"  Organizations: {len(orgs)} (kept as-is)")


if __name__ == "__main__":
    main()
