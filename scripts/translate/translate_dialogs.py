#!/usr/bin/env python3
"""Translate RE9 dialog files from English to Czech."""

import json
import os

OUTPUT_BASE = '/tmp/re9-translate/translations/natives/stm/message/dialog'

def write_translation(filename, translations):
    """Write translation dict to JSON file."""
    path = os.path.join(OUTPUT_BASE, filename)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(translations, f, ensure_ascii=False, indent=2)
    print(f"  Written {len(translations)} entries to {filename}")


def translate_mangm2():
    """dialog_mangm2.msg.23.json - Grace explores mansion, meets Emily."""
    return {
        # Grace alone, self-encouragement
        "ManGM2_c321s010_0010_ch0200": "Bude to dobrý.",
        "ManGM2_c321s010_0020_ch0200": "Doufám.",
        # Grace discovers horror
        "ManGM2_c321s020_0010_ch0200": "Bože můj...",
        "ManGM2_c321s020_0020_ch0200": "Co to proboha—?",
        # Emily (ch1300) - blind girl in a cell, stranger to Grace -> vykání from Grace initially
        "ManGM2_c321s020_0030_ch1300": "Kdo je tam?",
        "ManGM2_c321s020_0040_ch1300": "Je tam někdo?",
        "ManGM2_c321s020_0050_ch0200": "P-Promiňte, jestli jsem vás, ehm, vylekala.",
        "ManGM2_c321s020_0060_ch0200": "Šedý zákal...",
        "ManGM2_c321s020_0070_ch0200": "Vy nevidíte, že ne?",
        "ManGM2_c321s020_0080_ch1300": "Kdo jste?",
        "ManGM2_c321s020_0090_ch0200": "Byl v té druhé cele ještě někdo?",
        "ManGM2_c321s020_0100_ch0200": "Proč jste tam zavřená?",
        "ManGM2_c321s020_0110_ch1300": "Všichni jsou pryč.",
        # ch4010 = Hooded man
        "ManGM2_c321s020_0120_ch4010": "Nech ji být!",
        "ManGM2_c321s020_0130_ch0200": "Jste v pořádku!?",
        "ManGM2_c321s020_0140_ch4010": "Vypadni!",
        "ManGM2_c321s020_0150_ch4010": "Vypadni...",
        "ManGM2_c321s020_0160_ch0200": "Ne, ne! Počkejte!",
        "ManGM2_c321s020_0170_ch0200": "Ne! Ne, ne!",
        "ManGM2_c321s020_0180_ch0200": "To mě mrzí.",
        "ManGM2_c321s020_0190_ch0200": "Co se tu děje?",
        # Grace discovers clues
        "ManGM2_c321s700_0010_ch0200": "Ty dívky... Vypadají úplně jako...",
        "ManGM2_c321s700_0020_ch0200": "To vy jste ji zamkli.",
        "ManGM2_c321s700_0030_ch0200": "T-Tohle si půjčím.",
        "ManGM2_c321s700_0040_ch0200": "Vsadím se, že to dokáže přečíst.",
        # Grace approaches Emily more gently - switches to tykání with child
        "ManGM2_c321s800_0010_ch0200": "Hej...",
        "ManGM2_c321s800_0020_ch0200": "Proč tě tam zavřeli?",
        "ManGM2_c321s800_0030_ch1300": "Nevím. Vždycky jsem tu byla.",
        "ManGM2_c321s800_0040_ch0200": "Vadilo by ti, kdybych vešla?",
        "ManGM2_c321s800_0050_ch1300": "Ne...nevadí.",
        "ManGM2_c321s800_0060_ch0200": "Já... Tak, ehm...",
        "ManGM2_c321s800_0070_ch0200": "Promiň. Jsem od policie.",
        "ManGM2_c321s800_0080_ch1300": "...Policie?",
        "ManGM2_c321s800_0090_ch0200": "Ano... Chtěla bych, abys šla se mnou.",
        "ManGM2_c321s800_0100_ch1300": "Proč?",
        "ManGM2_c321s800_0110_ch0200": "Jsem Grace.",
        "ManGM2_c321s800_0120_ch0200": "Jak se jmenuješ?",
        "ManGM2_c321s800_0130_ch1300": "...Emily.",
        "ManGM2_c321s800_0140_ch0200": "Emily.",
        "ManGM2_c321s800_0150_ch0200": "Ráda čteš?",
        "ManGM2_c321s800_0160_ch1300": "Jo.",
        "ManGM2_c321s800_0170_ch0200": "Mohla bys mi něco přečíst?",
        "ManGM2_c321s800_0180_ch0200": "Prosím, o-opravdu potřebuju tvoji pomoc.",
        "ManGM2_c321s800_0190_ch1300": "...OK.",
        "ManGM2_c321s800_0200_ch0200": "Děkuju.",
        "ManGM2_c321s800_0210_ch0200": "Z-Zavedu tě tam.",
        "ManGM2_c321s800_0220_ch0200": "Jsou tam schody. Co kdybych tě odnesla?",
        # Puzzle section
        "ManGM2_c321s850_0010_ch0200": "Tady to je.",
        "ManGM2_c321s850_0020_ch0200": "Myslíš, že to dokážeš přečíst?",
        "ManGM2_c321s850_0030_ch1300": "Můžu to zkusit.",
        "ManGM2_c321s850_0040_ch0200": "Je to jako obří hlavolam!",
        "ManGM2_c321s850_0070_ch0200": "Zůstaň tady, Emily.",
        "ManGM2_c321s850_0080_ch0200": "Tady si poradíš ty.",
        "ManGM2_c321s850_0090_ch0200": "Já...",
        "ManGM2_c321s850_0100_ch0200": "se postarám...",
        "ManGM2_c321s850_0110_ch0200": "o tohle.",
        # Emily in danger
        "ManGM2_c321s900_0010_ch0200": "Jsem tady. Jsem tady.",
        "ManGM2_c321s900_0020_ch1300": "Našla jsem tohle.",
        "ManGM2_c321s900_0030_ch0200": "Výborně, Emily. Děkuju.",
        "ManGM2_c321s900_0050_ch0200": "Emily!?",
        "ManGM2_c321s900_0060_ch1300": "Pomozte mi! Pomoc!",
        "ManGM2_c321s900_0070_ch0200": "Emily!",
        # Aftermath
        "ManGM2_c321s950_0010_ch0200": "Za to všechno můžu já.",
        "ManGM2_c321s950_0020_ch0200": "Nemůžu ji tu nechat...",
        "ManGM2_c321s950_0030_ch0200": "Bože můj...",
        "ManGM2_c321s950_0040_ch0200": "OK.",
    }


def translate_movie():
    """dialog_movie.msg.23.json - Cinematic cutscenes."""
    return {
        # Song lyrics - keep ITALIC tags, translate poetically
        "Movie_c990s000_0010_dummy": "<ITALIC>Studený déšť mi prosakuje do duše</ITALIC>",
        "Movie_c990s000_0020_dummy": "<ITALIC>Staré rány, co nedokážu zapomenout</ITALIC>",
        "Movie_c990s000_0030_dummy": "<ITALIC>Noc mi bere zrak</ITALIC>",
        "Movie_c990s000_0040_dummy": "<ITALIC>Výkřiky, co nedokážu umlčet</ITALIC>",
        "Movie_c990s000_0050_dummy": "<ITALIC>Co kdybych k tobě byla natáhla ruku?</ITALIC>",
        "Movie_c990s000_0060_dummy": "<ITALIC>Nemusela bych jít sama</ITALIC>",
        "Movie_c990s000_0070_dummy": "<ITALIC>Bojuju s tmou, co mě svírá</ITALIC>",
        "Movie_c990s000_0080_dummy": "<ITALIC>Stahuje mě k zemi</ITALIC>",
        "Movie_c990s000_0090_dummy": "<ITALIC>Čelím bolesti, co mnou vládne</ITALIC>",
        "Movie_c990s000_0100_dummy": "<ITALIC>Nenechám se srazit na kolena</ITALIC>",
        "Movie_c990s000_0110_dummy": "<ITALIC>Dostanu se na druhou stranu</ITALIC>",
        "Movie_c990s000_0120_dummy": "<ITALIC>Zjizvené ruce, unavené a znavené</ITALIC>",
        "Movie_c990s000_0130_dummy": "<ITALIC>Teplo nového úsvitu na mé tváři</ITALIC>",
        "Movie_c990s000_0140_dummy": "<ITALIC>Už to nikdy nepustím</ITALIC>",
        # Grace at work - Nathan (ch1500) is her boss, vykání
        "Movie_c991s000_0030_ch0200": "J-Jestli jde o tu zprávu,\no kterou jste včera žádal,",
        "Movie_c991s000_0040_ch0200": "bude hotová za tři—",
        "Movie_c991s000_0050_ch0200": "ne, ne, za dva dny, maximálně.",
        # Nathan (ch1500) - Grace's boss
        "Movie_c991s000_0060_ch1500": "To teď odlož.",
        "Movie_c991s000_0070_ch1500": "Našli jsme další tělo.",
        "Movie_c991s000_0080_ch1500": "Vykazuje stejnou patologii jako\nostatní případy, co vyšetřujeme.",
        # Grace reacting
        "Movie_c991s000_0090_ch0200": "Chtěli mluvit se slečnou Ashcroftovou\na pak mi zavěsili.",
        "Movie_c991s000_0100_ch0200": "Drzost.",
        "Movie_c991s000_0110_ch0200": "Co to...?",
        "Movie_c991s000_0120_ch0200": "Chtěli mluvit se slečnou Ashcroftovou\na pak mi zavěsili.",
        "Movie_c991s000_0130_ch0200": "Drzost.",
        "Movie_c991s000_0140_ch0200": "Co to...?",
        # Alyssa (ch1800) - Grace's mother
        "Movie_c991s000_0150_ch1800": "Už jdou.",
        "Movie_c991s000_0160_ch1800": "Grace, musíme jít.",
        "Movie_c991s000_0170_ch0200": "Kam?",
        "Movie_c991s000_0180_ch0200": "Mami, co se děje?",
        "Movie_c991s000_0190_ch1800": "Pospěš!",
        "Movie_c991s000_0200_ch0200": "Počkej, kdo jde? Co se děje?",
        "Movie_c991s000_0210_ch1800": "Musíme mluvit potichu.",
        "Movie_c991s000_0220_ch0200": "To je absurdní.",
        "Movie_c991s000_0230_ch1800": "Pojď!",
        "Movie_c991s000_0240_ch0200": "C-Co mám dělat? Ehm...",
        "Movie_c991s000_0250_ch0200": "Do prdele...",
        # Cole (ch4030) - infected man
        "Movie_c991s000_0260_ch4030": "Nemůžu...",
        "Movie_c991s000_0270_ch0200": "Pojď!",
        "Movie_c991s000_0280_ch4030": "Jdi...tam!",
        "Movie_c991s000_0290_ch4030": "Nemůžu...jít...tam!",
        "Movie_c991s000_0300_ch0200": "H-Haló?",
        # Victor (ch5100) - main villain, vykání from Grace
        "Movie_c991s000_0310_ch5100": "Nebylo to snadné.",
        "Movie_c991s000_0320_ch5100": "Ale po velkém úsilí jsme konečně tady.",
        "Movie_c991s000_0330_ch0200": "Kdo jste?",
        "Movie_c991s000_0340_ch5100": "Teď už vím, že jste ta,\nkterou jsem celou dobu hledal.",
        "Movie_c991s000_0350_ch5100": "Ta výjimečná. Ta vyvolená.",
        "Movie_c991s000_0360_ch5100": "Slečna Ashcroftová.",
        # ch2110, ch2010 - unknown NPCs
        "Movie_c991s000_0370_ch2110": "Pomoc!",
        "Movie_c991s000_0380_ch2010": "Jsi v pořádku?",
        "Movie_c991s000_0390_ch2010": "Co to děláš!?",
        "Movie_c991s000_0400_ch0200": "Co to má být?",
        "Movie_c991s000_0410_ch0200": "Do prdele.",
        "Movie_c991s000_0420_ch0200": "Co to má být?",
        "Movie_c991s000_0430_ch0200": "Do prdele.",
        "Movie_c991s000_0440_ch0200": "Co to je?",
        "Movie_c991s000_0450_ch0200": "Hej! Pomoc!",
        "Movie_c991s000_0460_ch0200": "Ne... Ne, ne, ne...",
        "Movie_c991s000_0470_ch0200": "Tak dobře.",
        "Movie_c991s000_0480_ch0200": "Bože můj.",
        "Movie_c991s000_0490_ch0200": "Tak dobře.",
        "Movie_c991s000_0500_ch0200": "Bože můj.",
        "Movie_c991s000_0510_ch0200": "Bože, kolik jich je!",
        # Harry (ch1510) - helicopter pilot, tykání between them
        "Movie_c991s000_0520_ch1510": "Připoutej se!",
        "Movie_c991s000_0530_ch0200": "Emily, jsi v pořádku!?",
        "Movie_c991s000_0540_ch0200": "Emily.",
        # ch9922 = Operator
        "Movie_c991s000_0550_ch9922": "Posily jsou na cestě.",
        # ch0900 = ??? (mystery agent)
        "Movie_c991s000_0560_ch0900": "Není potřeba.\nCíl zneškodním sám.",
        "Movie_c991s000_0570_ch0200": "Nehýbej se!",
        "Movie_c991s000_0580_ch0200": "P-Počkej!",
        "Movie_c991s000_0590_ch0200": "Ještě mě potřebuješ, ne?",
        # Victor final scene
        "Movie_c991s000_0600_ch5100": "Ať se to celé zhroutí.",
        "Movie_c991s000_0610_ch5100": "Všechno.",
        # Leon (ch0100)
        "Movie_c991s000_0620_ch0100": "Grace.",
        "Movie_c991s000_0630_ch0100": "Grace!",
        "Movie_c991s000_0640_ch0100": "Je čas pohřbít poslední kostlivce Umbrella.",
    }


def translate_mangua():
    """dialog_mangua.msg.23.json - Grace escapes with Emily, meets Harry."""
    return {
        # Grace talking to Emily (child, tykání)
        "ManGUA_1000_0010_ch0200": "Hej, Emily, ehm... Nechtěla bys třeba...\nodejít se mnou?",
        "ManGUA_1000_0020_ch0200": "Tady to není bezpečný.",
        "ManGUA_1000_0030_ch1300": "Ehm... OK.",
        "ManGUA_1000_0040_ch0200": "Dobře. To je dobře.",
        "ManGUA_1100_0010_ch0200": "Nemůžu tu Emily nechat.",
        "ManGUA_1400_0010_ch0200": "Konečně...zvládly jsme to. Dokázaly jsme to...",
        "ManGUA_1500_0010_ch0200": "Emily? Jsi v pořádku?",
        "ManGUA_1500_0020_ch0200": "Emily?",
        "ManGUA_1500_0030_ch1300": "...Nevím.",
        "ManGUA_1500_0040_ch0200": "Tak prostě, ehm... Musíme jít dál,\ndobře? Emily?",
        "ManGUA_1500_0050_ch1300": "OK.",
        "ManGUA_1510_0010_ch0200": "Panebože...",
        # Meeting Harry (ch1510) - stranger initially, vykání then tykání quickly
        "ManGUA_c341s050_0010_ch1510": "Hej!",
        "ManGUA_c341s050_0020_ch1510": "Stůjte, kde jste.",
        "ManGUA_c341s050_0030_ch0200": "J-Je to v pořádku, n-nejsme nakažený...",
        "ManGUA_c341s050_0040_ch1510": "Takže jste normální?",
        "ManGUA_c341s050_0050_ch0200": "Ehm... M-Myslím, že jo.",
        "ManGUA_c341s050_0060_ch1510": "Díkybohu.",
        "ManGUA_c341s050_0070_ch1510": "Ty...věci ještě pobíhají venku?",
        "ManGUA_c341s050_0080_ch0200": "K-Kdo jste?",
        "ManGUA_c341s050_0090_ch1510": "O mě se nestarejte.",
        "ManGUA_c341s050_0100_ch1300": "Jsem unavená.",
        "ManGUA_c341s050_0110_ch0200": "Já vím.",
        "ManGUA_c341s050_0120_ch1510": "To je vaše dítě?",
        "ManGUA_c341s050_0130_ch0200": "Ehm, co je to—!?",
        "ManGUA_c341s050_0140_ch1510": "Tohle?",
        "ManGUA_c341s050_0150_ch1510": "Stará válečná vzpomínka.",
        "ManGUA_c341s050_0160_ch1510": "Utíkat nemůžu, ani kdybych chtěl.",
        "ManGUA_c341s050_0170_ch0200": "Umíte s tím lítat?",
        "ManGUA_c341s050_0180_ch1510": "Jasně. Ale ten zkurvený šéf mi vzal klíč.",
        # Switching to tykání as they cooperate
        "ManGUA_c341s050_0190_ch1510": "Víš co...",
        "ManGUA_c341s050_0200_ch1510": "Mohl bych nás všechny odsud odletět...",
        "ManGUA_c341s050_0210_ch1510": "jestli pro něj dojdeš.",
        "ManGUA_c341s050_0220_ch1510": "Je tam uvnitř.",
        "ManGUA_c341s050_0230_ch1510": "Šel bych sám, ale...",
        "ManGUA_c341s050_0240_ch1510": "s touhle nohou těm potvorám\nneutečeš.",
        "ManGUA_c341s050_0250_ch0200": "Nelžete mi?",
        "ManGUA_c341s050_0260_ch1510": "Cože?",
        "ManGUA_c341s050_0270_ch1510": "Viděla jsi to samý hovno co já!?",
        "ManGUA_c341s050_0280_ch1510": "Hele, paní, nemáme na výběr.",
        "ManGUA_c341s050_0290_ch1510": "Jak dlouho si myslíš,\nže tady ještě přežijeme?",
        "ManGUA_c341s050_0300_ch1300": "Můžu se vrátit k sobě do pokoje?",
        "ManGUA_c341s050_0310_ch0200": "Není to tam bezpečný.",
        "ManGUA_c341s050_0320_ch1510": "Hej... Můžeme si navzájem pomoct.",
        "ManGUA_c341s050_0330_ch1510": "Pohlídám ji...jestli donesete klíč.",
        "ManGUA_c341s050_0340_ch1510": "Uhlídám ji.",
        "ManGUA_c341s050_0350_ch1510": "Slibuju.",
        "ManGUA_c341s050_0360_ch0200": "D-Domluveno.",
        "ManGUA_c341s050_0370_ch0200": "Pojď.",
        "ManGUA_c341s050_0375_ch0200": "Mám tě.",
        "ManGUA_c341s050_0380_ch0200": "Připravená...?",
        "ManGUA_c341s050_0390_ch0200": "Ne, ne, ne.",
        "ManGUA_c341s050_0400_ch0200": "Pojď.",
        "ManGUA_c341s050_0410_ch0200": "Musím tě připoutat.",
        "ManGUA_c341s050_0415_ch0200": "Ach...ehm...",
        "ManGUA_c341s050_0420_ch0200": "J-Já jsem mimochodem Grace.",
        "ManGUA_c341s050_0430_ch0200": "T-Tohle je Emily.",
        "ManGUA_c341s050_0440_ch1510": "Harry.",
        "ManGUA_c341s050_0450_ch0200": "Děkuju, Harry.",
        "ManGUA_c341s050_0460_ch1510": "Není zač.",
        "ManGUA_c341s050_0470_ch0200": "Hned jsem zpátky.",
        # Harry yelling at Grace (tykání)
        "ManGUA_1513_0010_ch1510": "Co to sakra děláš!? Chceš mě zabít!?",
        "ManGUA_1514_0010_ch1510": "Au! Hej, přestaň blbnout!",
        "ManGUA_1515_0010_ch1510": "Zbláznilas se!?",
        "ManGUA_1516_0010_ch1510": "Hej! Mohla bys s tím klíčem pospíšit!?",
        "ManGUA_1517_0010_ch1510": "Co to děláš?\nŠéf vzal klíč tam dovnitř!",
        "ManGUA_1521_0010_ch0200": "Prosím...ať je tady.",
        "ManGUA_1540_0010_ch0200": "Aha, chápu.",
        "ManGUA_1550_0010_ch0200": "C-Cože!?",
    }


def translate_ff2nd():
    """dialog_ff2nd.msg.23.json - Chloe (ch0300) flashback in lab."""
    return {
        # Researchers panicking
        "FF2nd_c441s000_0010_ch9917": "Panebože!",
        "FF2nd_c441s000_0020_ch9918": "Musíme něco udělat!",
        "FF2nd_c441s000_0030_ch9917": "Volala jsem ostrahu, ale nikdo nebral.",
        "FF2nd_c441s000_0040_ch9918": "Nedají se ovládnout.",
        "FF2nd_c441s000_0050_ch9919": "Doktore, nedokážeme je zadržet!",
        "FF2nd_c441s000_0060_ch9918": "Podejte jim sedativa, hned!",
        "FF2nd_c441s000_0070_ch9917": "To nemyslíte vážně!?",
        "FF2nd_c441s000_0080_ch9918": "Uhněte mi z cesty!",
        # Chloe wakes up
        "FF2nd_c441s000_0090_ch0300": "Hej, jsi vzhůru?",
        "FF2nd_c441s000_0100_ch0300": "Cože?",
        "FF2nd_c441s000_0110_ch0300": "Kam všichni odešli?",
        # Researcher panicking
        "FF2nd_c441s200_0010_ch9920": "Nechoďte blíž! Nechoďte blíž!",
        "FF2nd_c441s200_0020_ch9920": "Zpátky!",
        "FF2nd_c441s200_0030_ch9920": "Nepřibližujte se!",
        "FF2nd_c441s200_0040_ch9920": "Ne...",
        "FF2nd_c441s200_0050_ch9920": "Ne! Zpátky!",
        "FF2nd_c441s200_0060_ch9920": "Zpátky!",
        "FF2nd_c441s200_0070_ch0300": "Hej!",
        "FF2nd_c441s200_0080_ch0300": "Co to děláš!?",
        # Chloe alone, scared (child)
        "FF2nd_0150_0010_ch0300": "Vždyť tu byli před chvílí?",
        "FF2nd_0160_0010_ch0300": "Ale je po večerce.",
        "FF2nd_0200_0010_ch0300": "C-Co to bylo?",
        "FF2nd_0210_0010_ch0300": "M-Musím se schovat.",
        "FF2nd_0310_0010_ch0300": "Prosím... Někdo mi pomozte.",
        "FF2nd_0350_0010_ch0300": "Nehýbe se...",
        "FF2nd_0440_0010_ch0300": "Prosím, otevřete se!",
        "FF2nd_0550_0010_ch0300": "Nesmí mě najít!",
        "FF2nd_0647_0020_ch0300": "C-Co mám dělat!? Co mám dělat!?",
        "FF2nd_0670_0010_ch0300": "Jsou pryč?",
        "FF2nd_0750_0020_ch0300": "Prosím, ať je to jenom zlý sen.",
        "FF2nd_0750_0030_ch0300": "P-Proč oni...",
        "FF2nd_0750_0040_ch0300": "Kde to jsem?",
        "FF2nd_0810_0010_ch0300": "Jak se odsud dostanu?",
        "FF2nd_1210_0010_ch0300": "C-Co je s nimi!?",
        "FF2nd_1300_0010_ch0300": "C-Co... Co je tohle za místo?",
        "FF2nd_1320_0010_ch0300": "Nejde to otevřít.",
        "FF2nd_1400_0010_ch0300": "To jsou...miminka?",
        # ch9921 = Researcher B
        "FF2nd_c441s800_0010_ch9921": "Chloe?",
        "FF2nd_c441s800_0020_ch0300": "Takhle jsem—?",
        "FF2nd_c441s800_0030_ch9921": "Mám ji!",
        "FF2nd_c441s800_0040_ch9921": "Pojďte sem, hned!",
        "FF2nd_c441s800_0050_ch9921": "Má příznaky taky.",
        "FF2nd_c441s800_0060_ch9921": "Musíme se jí zbavit.",
    }


def translate_underhb():
    """dialog_underhb.msg.23.json - Leon in underground, meets Zeno, fights mystery agent."""
    return {
        "UnderHB_1010_0010_ch0100": "Licker!",
        "UnderHB_c510s200_0010_ch0100": "Kde to je?",
        "UnderHB_c510s200_0020_ch0100": "OK.",
        "UnderHB_c510s200_0030_ch0100": "Hm?",
        "UnderHB_1100_0010_ch0100": "Mám pocit, že mě tu moc\nnechtějí.",
        # Announcement (ch9916)
        "UnderHB_2000_0010_ch9916": "Zde v ARK bude váš pohyb\nneustále monitorován.",
        "UnderHB_2000_0020_ch9916": "Bez povolení neopouštějte\nvyhrazené prostory.",
        "UnderHB_2000_0030_ch9916": "Zaznamenávání a přenos informací\nje přísně zakázán.",
        "UnderHB_1290_0010_ch0100": "Grace by měla být hned za rohem.",
        # ch9922 = Operator, ch0900 = mystery agent
        "UnderHB_c510s400_0010_ch9922": "Posily jsou na cestě.",
        "UnderHB_c510s400_0020_ch0900": "Není potřeba.\nCíl zneškodním sám.",
        "UnderHB_c510s400_0030_ch0900": "Leon Kennedy.",
        "UnderHB_c510s400_0040_ch0900": "Konečně se setkáváme.",
        # Leon vs mystery agent - cocky Leon, vykání from agent
        "UnderHB_5000_0010_ch0100": "Netušil jsem, že mám tak velkýho\nfanouška. Co takhle autogram?",
        "UnderHB_5000_0020_ch0900": "Slyšel jsem, že umíš kecat.",
        "UnderHB_5010_0010_ch0900": "Nešpatné na někoho, kdo má\njednu nohu v hrobě.",
        "UnderHB_5010_0020_ch0100": "Děláš si o mě starosti? To je milý.",
        "UnderHB_5020_0010_ch0100": "Zákeřnej zmrd.",
        "UnderHB_5030_0010_ch0100": "Trochu moc osahávání, ne?",
        "UnderHB_5030_0020_ch0900": "Nemylte se. Nic mi nestojí v cestě.\nTuhle misi dokončím.",
        "UnderHB_5040_0010_ch0100": "Narazil jsem na problém. Tenhle chlap\nbyl zatraceně tvrdej oříšek.",
        "UnderHB_5040_0020_ch0600": "Od tebe je to pořádnej kompliment.",
        "UnderHB_5045_0010_ch0100": "Grace by měla být blízko.\nČas konečně dostat odpovědi.",
        "UnderHB_5050_0010_ch0900": "Cíl zneškodněn. Mise splněna.",
        # Zeno (ch8000) - scientist, formal, vykání
        "UnderHB_c510s900_0010_ch8000": "Grace, tady právě jsme.",
        "UnderHB_c510s900_0020_ch8000": "Svět je v ohrožení.",
        "UnderHB_c510s900_0030_ch8000": "Technologie k ovládání\ncizí vůle už existuje.",
        "UnderHB_c510s900_0040_ch8000": "Ale není efektivní při šíření nákazy.",
        "UnderHB_c510s900_0050_ch8000": "Věřím, že Spencer to vyřešil pomocí Elpis.",
        "UnderHB_c510s900_0060_ch8000": "The Connections zapečetili Raccoon\nCity, aby si ho nechali pro sebe.",
        "UnderHB_c510s900_0070_ch8000": "A od té doby to tu čeká.",
        "UnderHB_c510s900_0080": "\"Co si přeje tvůrce?\"",
        "UnderHB_c510s900_0090_ch8000": "Tady jsme se zasekli.",
        "UnderHB_c510s900_0100_ch8000": "Pokud se zadá špatné heslo, ARK bude\nzničen a Elpis bude navždy ztracena.",
        "UnderHB_c510s900_0110_ch8000": "Tak mi řekněte, Grace.",
        "UnderHB_c510s900_0120_ch8000": "Jaké je heslo?",
        "UnderHB_c510s900_0130_ch0200": "N-Nevím.",
        "UnderHB_c510s900_0140_ch8000": "Samozřejmě, že víte. Vy jste přece—",
        "UnderHB_c510s900_0150_ch0200": "Leone!",
        "UnderHB_c510s900_0160_ch8000": "Nedělejte ze sebe ostudu, pane Kennedy.",
        "UnderHB_c510s900_0170_ch8000": "Nemůžete mě porazit.",
        "UnderHB_c510s900_0180_ch0100": "Ale, ale, jaká paráda.",
        "UnderHB_c510s900_0190_ch0200": "Nehýbej se!",
        "UnderHB_c510s900_0200_ch0200": "P-Počkej!",
        "UnderHB_c510s900_0210_ch0200": "Ještě mě potřebuješ, ne?",
        # Leon and Grace escaping
        "UnderHB_c510s900_0220_ch0100": "Pojď!",
        "UnderHB_c510s900_0230_ch0100": "Drž se!",
        "UnderHB_c510s900_0240_ch0100": "Mám tě.",
        "UnderHB_c510s900_0250_ch0200": "Jsi v pořádku?",
        "UnderHB_c510s900_0260_ch0100": "Já?",
        "UnderHB_c510s900_0270_ch0100": "Cítím se skvěle.",
        "UnderHB_c510s900_0280_ch0200": "Kam to vede?",
        "UnderHB_c510s900_0290_ch0100": "Tvůj odhad je stejně dobrej jako můj.",
        "UnderHB_c510s900_0300_ch0100": "Čas vystoupit. Pojď.",
        "UnderHB_c510s900_0310_ch0200": "Co teď?",
        "UnderHB_c510s900_0315_ch0200": "Leone?",
        "UnderHB_c510s900_0320_ch0200": "Leone!",
    }


def translate_battlepl():
    """dialog_battlepl.msg.23.json - Battle barks for Leon (ch0100) and Grace (ch0200)."""
    return {
        # Leon hurt/damaged barks
        "BattlePL_1001_0010_ch0100": "Do prdele.",
        "BattlePL_1002_0010_ch0100": "Musím něco vymyslet.",
        "BattlePL_1003_0010_ch0100": "Přehnal jsem to.",
        "BattlePL_1005_0010_ch0100": "Kurva, to je blbý.",
        "BattlePL_1006_0010_ch0100": "Ty zmetku...",
        "BattlePL_1007_0010_ch0100": "Výborně...",
        "BattlePL_1008_0010_ch0100": "Ještě nekončím.",
        # Leon healed/recovery barks
        "BattlePL_1102_0010_ch0100": "To zabralo.",
        "BattlePL_1103_0010_ch0100": "Tak jdeme na to.",
        "BattlePL_1104_0010_ch0100": "Dobře.",
        "BattlePL_1106_0010_ch0100": "Takovej špatnej to není.",
        "BattlePL_1107_0010_ch0100": "Můžu pokračovat.",
        "BattlePL_1109_0010_ch0100": "OK.",
        "BattlePL_1110_0010_ch0100": "Ještě stojím.",
        "BattlePL_1111_0010_ch0100": "Ještě...jsem ve hře.",
        # Leon last item barks
        "BattlePL_1801_0010_ch0100": "To byl poslední.",
        "BattlePL_1802_0010_ch0100": "Už nemám nic.",
        "BattlePL_1803_0010_ch0100": "Sakra, došly mi.",
        "BattlePL_1804_0010_ch0100": "Poslední.",
        # Leon out of ammo
        "BattlePL_1901_0010_ch0100": "Hodil by se mi náboj.",
        "BattlePL_1902_0010_ch0100": "Nemám náboje.",
        "BattlePL_1903_0010_ch0100": "Potřebuju náboje.",
        "BattlePL_1904_0010_ch0100": "Sakra, prázdný.",
        # Leon hatchet broken
        "BattlePL_2000_0010_ch0100": "Kurva, moje sekyrka.",
        "BattlePL_2001_0010_ch0100": "Sekyrka...",
        "BattlePL_2002_0010_ch0100": "Zlomila se mi ta zatracená sekyrka.",
        # Leon throwing barks
        "BattlePL_2201_0010_ch0100": "Tady.",
        "BattlePL_2202_0010_ch0100": "Chyť.",
        "BattlePL_2203_0010_ch0100": "Sežer to.",
        "BattlePL_2204_0010_ch0100": "Na, máš.",
        # Grace hurt/damaged barks
        "BattlePL_5001_0010_ch0200": "Sakra.",
        "BattlePL_5002_0010_ch0200": "To je špatný.",
        "BattlePL_5003_0010_ch0200": "Pusť mě!",
        "BattlePL_5004_0010_ch0200": "Ne.",
        "BattlePL_5005_0010_ch0200": "Vydrž...",
        "BattlePL_5006_0010_ch0200": "To je blbý.",
        "BattlePL_5007_0010_ch0200": "Do háje.",
        "BattlePL_5008_0010_ch0200": "Kurva, to bolí.",
        "BattlePL_5009_0010_ch0200": "Musím zůstat v klidu.",
        "BattlePL_5010_0010_ch0200": "Zvládneš to.",
        # Grace healed/recovery barks
        "BattlePL_5101_0010_ch0200": "To je lepší.",
        "BattlePL_5102_0010_ch0200": "Jsi OK, jsi OK.",
        "BattlePL_5103_0010_ch0200": "Dám to.",
        "BattlePL_5104_0010_ch0200": "Díkybohu.",
        "BattlePL_5105_0010_ch0200": "Mnohem lepší.",
        "BattlePL_5107_0010_ch0200": "To bylo o fous.",
        "BattlePL_5108_0010_ch0200": "Dobře.",
        "BattlePL_5109_0010_ch0200": "Dobře, jsem v pohodě.",
        "BattlePL_5110_0010_ch0200": "Ještě nekončím.",
        # Grace throwing barks
        "BattlePL_5901_0010_ch0200": "No tak.",
        "BattlePL_5902_0010_ch0200": "Netrefím se.",
        "BattlePL_5903_0010_ch0200": "Prosím, zabír.",
        # Grace out of ammo
        "BattlePL_6001_0010_ch0200": "Ne. Potřebuju náboje.",
        "BattlePL_6002_0010_ch0200": "Nemám náboje.",
        "BattlePL_6003_0010_ch0200": "Ne, jsem prázdná.",
        "BattlePL_6004_0010_ch0200": "Musím najít víc nábojů.",
        "BattlePL_6005_0010_ch0200": "Prázdný.",
        # Grace last item
        "BattlePL_6101_0010_ch0200": "Snad mi to vystačí.",
        "BattlePL_6102_0010_ch0200": "To byl poslední.",
        "BattlePL_6103_0010_ch0200": "Ach... Už mi žádný nezbývá.",
        "BattlePL_6104_0010_ch0200": "Poslední.",
    }


def translate_manlc():
    """dialog_manlc.msg.23.json - Leon finds Grace, they escape together."""
    return {
        # Leon calling Sherry (ch0600) - tykání between them (old friends)
        "ManLC_1005_0010_ch0100": "Sherry, Grace je pořád tady.",
        "ManLC_1005_0020_ch0600": "Ta agentka FBI?",
        "ManLC_1005_0030_ch0100": "Jo. Našel jsem soubory ve Victorově\npočítači. Nějak s tím souvisí.",
        "ManLC_1015_0010_ch0600": "Je v pořádku?",
        "ManLC_1015_0020_ch0100": "Ne, ale pohlídám ji.",
        "ManLC_1023_0010_ch0100": "Další.",
        "ManLC_1024_0010_ch0100": "Trefa.",
        "ManLC_1025_0010_ch0100": "OK.",
        "ManLC_1030_0010_ch0100": "Vypadá to, že šli napřed.",
        "ManLC_1035_0010_ch0100": "Asi je čas na večerní bohoslužbu.",
        "ManLC_1036_0010_ch0100": "Vydrž, Grace.",
        "ManLC_1040_0010_ch0100": "Dobře.",
        "ManLC_1050_0010_ch0100": "S dovolením.",
        "ManLC_3076_0010_ch0100": "Dokáže mutovat ostatní.",
        "ManLC_1080_0010_ch0100": "Čas uklidit zbytek.",
        # Grace in danger
        "ManLC_2000_0010_ch0200": "Nechte nás být!",
        "ManLC_2010_0010_ch0200": "Ugh... Pomoc! Pomoc!",
        "ManLC_2020_0010_ch0200": "Pusť mě!",
        # Leon and Grace meet
        "ManLC_c342s800_0010_ch0200": "Vydrž se mnou.",
        "ManLC_c342s800_0020_ch0200": "Bože.",
        "ManLC_c342s800_0030_ch0100": "Grace.",
        "ManLC_c342s800_0040_ch0200": "Leone!",
        "ManLC_c342s800_0050_ch0100": "Kdo je to?",
        "ManLC_c342s800_0060_ch0200": "To je Emily.",
        "ManLC_c342s800_0070_ch0200": "Pomoz mi! N-Nemůžu zastavit krvácení.",
        "ManLC_c342s800_0080_ch0100": "Hej, hej, koukej na mě.",
        "ManLC_c342s800_0090_ch0100": "Bude to dobrý.",
        "ManLC_c342s800_0100_ch0100": "Jo?",
        "ManLC_c342s800_0110_ch0100": "Tady zůstat nemůžeme.",
        "ManLC_c342s800_0120_ch0100": "Támhle by měla být cesta\nk čistírně vody.",
        "ManLC_c342s800_0130_ch0100": "To je náš způsob ven.",
        "ManLC_c342s800_0140_ch0100": "Jdeme.",
        "ManLC_c342s800_0150_ch0100": "Prostě se nevzdávají.",
        "ManLC_c342s800_0160_ch0100": "Vezmi ji.",
        "ManLC_c342s800_0170_ch0100": "Dostaň ji do bezpečí.",
        "ManLC_c342s800_0180_ch0100": "Běž!",
        "ManLC_c342s800_0190_ch0100": "Hned!",
        "ManLC_c342s800_0200_ch0100": "Naše přátele tu zabavím.",
        # Leon discovers Elpis
        "ManLC_c342s000_0010_ch0100": "Elpis?",
        "ManLC_c342s000_0020_ch0100": "Grace?",
        "ManLC_c342s000_0030_ch0100": "Co s tím má společnýho?",
        "ManLC_c342s000_0040_ch0100": "Nazdar, kočko.",
        "ManLC_c342s000_0050_ch0200": "Pojď, Emily.",
        "ManLC_c342s000_0060_ch0200": "Do prdele.",
        "ManLC_c342s000_0070_ch0100": "Ta holka se prostě nemůže vyhnout problémům.",
    }


def translate_centba():
    """dialog_centba.msg.23.json - Leon in Raccoon City center, talking to Sherry."""
    return {
        # Leon and Sherry (tykání - old friends)
        "CentBA_c410s200_0010_ch0600": "Hej, hlásím se.",
        "CentBA_c410s200_0020_ch0100": "Zrovna včas.",
        "CentBA_c410s200_0030_ch0100": "Našla jsi něco o Elpis?",
        "CentBA_c410s200_0040_ch0600": "Zatím ne.",
        "CentBA_c410s200_0050_ch0600": "Nic na serverech CIA\nani Pentagonu.",
        "CentBA_c410s200_0060_ch0100": "Možná potřebujeme vyšší oprávnění.",
        "CentBA_c410s200_0070_ch0600": "Zažádala jsem o něj a řekli mi,\nať vyšetřování zastavím.",
        "CentBA_c410s200_0080_ch0100": "Cože? Proč?",
        "CentBA_c410s200_0090_ch0600": "Neřekli.",
        "CentBA_c410s200_0100_ch0600": "Rozkaz shora.",
        "CentBA_c410s200_0110_ch0100": "Hele, nechci, abys kvůli tomu měla\npotíže. Půjdu do toho sám.",
        "CentBA_c410s200_0120_ch0600": "Jsme v tom spolu. Až do konce.",
        "CentBA_c410s200_0130_ch0600": "Vždycky jsem uměla\npracovat ve stínu.",
        "CentBA_c410s200_0140_ch0100": "Jenom nic moc riskantního, jo?",
        "CentBA_c410s200_0150_ch0600": "Já? Nikdy.",
        "CentBA_c410s200_0160_ch0100": "Půjdu najít Grace.",
        "CentBA_c410s200_0170_ch0100": "Určitě má něco společnýho s Elpis.",
        "CentBA_c410s201_0010_ch0100": "Tak, silnice je pryč.",
        "CentBA_c410s201_0020_ch0100": "Budu muset najít jinou cestu.",
        "CentBA_c410s201_0030_ch0600": "Dobře. To nechám na tobě.",
        "CentBA_c410s201_0040_ch0600": "Myslím, že jsem našla stopu,\nkde by mohli být.",
        "CentBA_c410s201_0050_ch0600": "Nějaké souřadnice ve Victorově počítači.",
        "CentBA_c410s201_0060_ch0100": "Mám to, díky.",
        "CentBA_c410s201_0070_ch0600": "Přímo v centru Raccoon City.",
        "CentBA_5000_0010_ch0100": "Ne, tudy ne.",
        # Leon arrives at Raccoon City
        "CentBA_c410s300_0010_ch0100": "Kurva.",
        "CentBA_c410s300_0020_ch0100": "Do prdele.",
        "CentBA_0025_0010_ch0100": "Jako by se tu zastavil čas.",
        "CentBA_0025_0020_ch0600": "Nebýt Umbrella, mohlo to\nbýt normální město.",
        "CentBA_0025_0030_ch0100": "Jo. Teď je tu jen popel a vzpomínky.",
        "CentBA_0038_0010_ch0100": "Dobře, co dál?",
        "CentBA_0060_0010_ch0100": "Ty jsi ale pěknej otravák, víš to?",
        "CentBA_0065_0010_ch0100": "Asi tě budu muset rozšlápnout.",
        "CentBA_0090_0010_ch0100": "Kde seš?",
        "CentBA_1000_0010_ch0100": "Proč si nenajdeš někoho jiného k okusování?",
        "CentBA_1020_0010_ch0100": "Nikdo tě neučil slušnému chování?",
        "CentBA_1040_0010_ch0100": "Ještě ti to nestačí? Na hubení\nhmyzu nemám čas.",
        "CentBA_c410s900_0020_ch0100": "Ta pohostinnost Raccoon City mi chyběla.",
    }


def translate_mange():
    """dialog_mange.msg.23.json - Grace wakes up captive, escapes."""
    return {
        "ManGE_c311s101_0010_ch0200": "Ne...",
        "ManGE_c311s101_0020_ch0200": "Ne!",
        "ManGE_c311s101_0040_ch0200": "Co to má být?",
        "ManGE_c311s101_0050_ch0200": "Do prdele.",
        "ManGE_c311s101_0060_ch0200": "Co to je?",
        "ManGE_c311s101_0070_ch0200": "Hej! Pomoc!",
        "ManGE_c311s101_0080_ch0200": "Ne... Ne, ne, ne...",
        "ManGE_c311s101_0090_ch0200": "Musíš zůstat v klidu.",
        "ManGE_c311s101_0100_ch0200": "Musíš zachovat chladnou hlavu. Tak.",
        "ManGE_c311s101_0110_ch0200": "Mysli.",
        "ManGE_c311s101_0120_ch0200": "Mysli, Grace, mysli.",
        "ManGE_c311s101_0130_ch0200": "Ano.",
        "ManGE_c311s101_0150_ch0200": "Ano!",
        "ManGE_c311s101_0160_ch0200": "No tak.",
        "ManGE_c311s101_0180_ch0200": "Co mi to udělal?",
        "ManGE_c311s101_0190_ch0200": "No tak.",
        "ManGE_0060_0010_ch0200": "Kde to sakra jsem?",
        "ManGE_0070_0010_ch0200": "Mrtvej.",
        "ManGE_0290_0010_ch0200": "Někde mi muselo něco uniknout.",
        "ManGE_c311s250_0010_ch0200": "Je mrtvej.",
        "ManGE_c311s250_0020_ch0200": "Nakažený.",
        "ManGE_0470_0010_ch0200": "Kurva! C-Co to je za sračku!?",
        "ManGE_0511_0010_ch0200": "Ježíši!",
        "ManGE_0600_0010_ch0200": "Co to sakra bylo za věc!?",
        "ManGE_0650_0010_ch0200": "Možná bych měla zkontrolovat tu\nmístnost, kde byla ta...věc.",
        "ManGE_0680_0010_ch0200": "Bože... Panebože.",
        "ManGE_0683_0010_ch0200": "Kurva!",
        "ManGE_0686_0010_ch0200": "Tudy ne. Tudy ne. Tudy ne.",
        "ManGE_0690_0010_ch0200": "Sakra!",
        "ManGE_0700_0010_ch0200": "Ano!",
        "ManGE_0730_0010_ch0200": "Prosím, ne...",
        "ManGE_c311s510_0010_ch0200": "Tak dobře.",
        "ManGE_c311s510_0020_ch0200": "Bože můj.",
        "ManGE_c311s610_0010_ch0200": "No tak, no tak, no tak,\nno tak, no tak!",
        "ManGE_c311s610_0020_ch0200": "Pusť mě!",
        "ManGE_4000_0010_ch0200": "Tohle vypadá důležitě...možná.",
        "ManGE_4005_0010_ch0200": "Asi neuškodí pár utrhnout.",
        "ManGE_4100_0010_ch0200": "Ještě nechci umřít...",
    }


def translate_platform():
    """dialog_platform.msg.23.json - Generic platform/puzzle barks."""
    return {
        "Platform_0010_0010_dummy": "To pomohlo!",
        "Platform_0020_0010_dummy": "Díky. Ehm...děkuju.",
        "Platform_0030_0010_dummy": "N-Neboj, je to OK.",
        "Platform_0040_0010_dummy": "Výborně!",
        "Platform_0050_0010_dummy": "Jsem tady. Jsem tady.",
        "Platform_0060_0010_dummy": "Vzpomeň si na výcvik, Grace.",
        "Platform_0070_0010_dummy": "To pomohlo!",
        "Platform_0080_0010_dummy": "Moment.",
        "Platform_0090_0010_dummy": "Aha, chápu.",
        "Platform_0100_0010_dummy": "Ehm... M-Myslím, že jo.",
        "Platform_0110_0010_dummy": "Tohle vypadá důležitě...možná.",
        "Platform_0120_0010_dummy": "Co to je?",
        "Platform_0130_0010_dummy": "Klid, Grace...",
        "Platform_0140_0010_dummy": "Mysli...",
        "Platform_0150_0010_dummy": "Cože? Já, ehm, já—",
        "Platform_0160_0010_dummy": "Možná mi něco uniká...",
        "Platform_0170_0010_dummy": "Kde jsem to viděla...?",
        "Platform_0180_0010_dummy": "Ach ne!",
        "Platform_0190_0010_dummy": "Co to je?",
        "Platform_0200_0010_dummy": "Dobře, tohle se hodí.",
        "Platform_0210_0010_dummy": "Tak snadno se nevzdávám.",
        "Platform_0220_0010_dummy": "Hele, já to chápu. Věř mi, chápu to.",
        "Platform_0230_0010_dummy": "Příběh mého života.",
        "Platform_0240_0010_dummy": "Heh... Tady se člověk nenudí.",
        "Platform_0250_0010_dummy": "Dneska mám štěstí.",
        "Platform_0260_0010_dummy": "Dobře, tohle se hodí.",
        "Platform_0270_0010_dummy": "Dobře, co dál?",
        "Platform_0280_0010_dummy": "Pokaždý.",
        "Platform_0290_0010_dummy": "Ne, tudy ne.",
        "Platform_0300_0010_dummy": "No, to dopadlo skvěle.",
        "Platform_0310_0010_dummy": "Na tohle nemám čas.",
        "Platform_0320_0010_dummy": "Vážně.",
        "Platform_0330_0010_dummy": "Ne... Ne, tohle je jiný.",
        "Platform_0340_0010_dummy": "Co to je?",
        "Platform_0350_0010_dummy": "Být slavná je těžký.",
        "Platform_0360_0010_dummy": "Nazdar, kočko.",
        "Platform_0370_0010_dummy": "Tebe si pamatuju.",
        "Platform_0380_0010_dummy": "Tenhle den je pořád lepší a lepší.",
        "Platform_0390_0010_dummy": "To si nenechám ujít.",
    }


def translate_centuc():
    """dialog_centuc.msg.23.json - Leon underground cavern."""
    return {
        "CentUC_0030_0010_ch0100": "Vážně.",
        "CentUC_0040_0010_ch0100": "Vypadá to, že vystupuju tady.",
        "CentUC_0045_0010_ch0100": "BSAA tu po sobě něco nechali.",
        "CentUC_0046_0010_ch0100": "Tohle nekončí.",
        "CentUC_0060_0010_ch0100": "Konečně jsem na dně.\nTo je sakra hluboká díra.",
        "CentUC_0060_0020_ch0600": "Ideální místo, kde něco schovat.",
        "CentUC_0067_0010_ch0100": "Tyhle kytky mě fakt nemají rády.",
        "CentUC_0070_0010_ch0100": "Jen abys věděla, každá rostlina,\nco jsem kdy měl, mi uhynula.",
        "CentUC_0077_0010_ch0100": "Ty jsi ale tvrdohlavej plevel.",
        "CentUC_0077_0020_ch0100": "Čas tě vypálit i s kořenama!",
        "CentUC_0080_0010_ch0100": "Tohle musí být ono.",
        "CentUC_c450s900_0010_ch0100": "Sherry, našel jsem nějaký\nobrovský zařízení.",
        "CentUC_c450s900_0020_ch0600": "Co myslíš, že to je?",
        "CentUC_c450s900_0030_ch0100": "Vidím zásoby s logy\nobvyklých podezřelých.",
        "CentUC_c450s900_0040_ch0600": "Ať už je to cokoliv,\nzjevně to nemělo být nalezeno.",
        "CentUC_c450s900_0050_ch0100": "Jo, to mi říkáš.",
    }


def translate_centhw():
    """dialog_centhw.msg.23.json - Leon highway/driving section."""
    return {
        "CentHW_1001_0010_ch0100": "Dobře, měl bych tam být co nevidět.",
        "CentHW_1001_0020_ch0600": "To ráda slyším. Jaký jsou silnice?",
        "CentHW_1002_0010_ch0600": "Leone?",
        "CentHW_1002_0020_ch0100": "Jenom pár...výmolů.",
        "CentHW_1015_0010_ch0100": "Tenhle den je pořád lepší a lepší.",
        "CentHW_1048_0010_ch0100": "Tihle pejsci potřebujou víc výcviku.",
        "CentHW_1062_0010_ch5100": "Zemři, hlupče!",
        "CentHW_1065_0010_ch0100": "Ježíši!",
        "CentHW_1166_0020_ch0100": "Tak tolik k přímý cestě.",
        "CentHW_1068_0010_ch0100": "Zase. Vážně?",
        "CentHW_1068_0020_ch0100": "Tak snadno se nevzdávám.",
        "CentHW_c430s800_0010_ch5100": "Mám tě dost!",
        "CentHW_c430s800_0020_ch0100": "Já tebe taky!",
        "CentHW_c430s800_0030_ch5100": "Pojď!",
        "CentHW_c430s950_0020_ch0100": "Měl jsem si vzít helmu.",
    }


def translate_ending():
    """dialog_ending.msg.23.json - Ending scenes."""
    return {
        # Grace on phone, talking about Sherry (vykání not needed - she asks about a friend)
        "Ending_c540s200_0010_ch0200": "A Sherry je v pořádku?",
        "Ending_c540s200_0020_ch0200": "Dobře, to jsem ráda.",
        "Ending_c540s200_0030_ch0200": "Emily?",
        "Ending_c540s200_0040_ch0200": "Jo, ehm, daří se jí skvěle.",
        "Ending_c540s200_0050_ch0200": "Vlastně ji učím číst.",
        # Nathan (ch1500) - boss
        "Ending_c540s200_0060_ch1500": "Grace!",
        "Ending_c540s200_0070_ch1500": "Grace!",
        "Ending_c540s200_0080_ch1500": "Kde je ta zpráva?",
        "Ending_c540s200_0090_ch0200": "Pardon.",
        "Ending_c540s200_0100_ch0200": "Leone, musím jít. Brzy se ozvem.",
        # Post-credits
        "Ending_c540s400_0010_ch9927": "Hej! Ozvěte se! Jaký je váš stav!?",
        "Ending_c540s400_0020_ch9928": "Zbývající síly BSAA byly zneškodněny.",
        "Ending_c540s400_0030_ch9928": "Zajišťuji cíl, než\npošlou \"vlky.\"",
    }


def translate_reactionspl():
    """dialog_reactionspl.msg.23.json - Player reactions."""
    return {
        # Rejected entries - keep as-is with tags
        "ReactionsPL_1900_0000": "<COLOR FF0000>#Rejected#</COLOR> ReactionsPL_1900_0000",
        "ReactionsPL_1900_0010_ch0200": "<COLOR FF0000>#Rejected#</COLOR> ReactionsPL_1900_0010_ch0200",
        "ReactionsPL_1901_0000": "<COLOR FF0000>#Rejected#</COLOR> ReactionsPL_1901_0000",
        "ReactionsPL_1901_0010_ch0200": "<COLOR FF0000>#Rejected#</COLOR> ReactionsPL_1901_0010_ch0200",
        "ReactionsPL_1902_0000": "<COLOR FF0000>#Rejected#</COLOR> ReactionsPL_1902_0000",
        "ReactionsPL_1902_0010_ch0200": "<COLOR FF0000>#Rejected#</COLOR> ReactionsPL_1902_0010_ch0200",
        # Actual dialog
        "ReactionsPL_2000_0010_ch0200": "Nechoď blíž!",
        "ReactionsPL_2100_0010_ch0200": "Ne.",
        "ReactionsPL_2200_0010_ch0200": "Co to kurva!?",
    }


def main():
    translations = {
        'dialog_mangm2.msg.23.json': translate_mangm2(),
        'dialog_movie.msg.23.json': translate_movie(),
        'dialog_mangua.msg.23.json': translate_mangua(),
        'dialog_ff2nd.msg.23.json': translate_ff2nd(),
        'dialog_underhb.msg.23.json': translate_underhb(),
        'dialog_battlepl.msg.23.json': translate_battlepl(),
        'dialog_manlc.msg.23.json': translate_manlc(),
        'dialog_centba.msg.23.json': translate_centba(),
        'dialog_mange.msg.23.json': translate_mange(),
        'dialog_platform.msg.23.json': translate_platform(),
        'dialog_centuc.msg.23.json': translate_centuc(),
        'dialog_centhw.msg.23.json': translate_centhw(),
        'dialog_ending.msg.23.json': translate_ending(),
        'dialog_reactionspl.msg.23.json': translate_reactionspl(),
    }

    for filename, data in translations.items():
        write_translation(filename, data)

    print(f"\nDone! Translated {len(translations)} files.")


if __name__ == '__main__':
    main()
