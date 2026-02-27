#!/usr/bin/env python3
"""Translate all RE9 soundsupport subtitle files from English to Czech."""

import json
import os

SRC_DIR = "json/natives/stm/message/soundsupport/"
OUT_DIR = "translations/natives/stm/message/soundsupport/"

os.makedirs(OUT_DIR, exist_ok=True)

# Master translation dictionary for sound effect descriptions
# These are subtitle annotations for audio - keep character names in English
TRANSLATIONS = {
    # === Common sound effects ===
    "[swallowing]": "[polykání]",
    "[sigh]": "[povzdech]",
    "[sighs]": "[vzdychá]",
    "[bones crack]": "[praskání kostí]",
    "[spider chittering]": "[šramocení pavouka]",
    "[roar]": "[řev]",
    "[squeal]": "[výkřik]",
    "[thud]": "[úder]",
    "[rumbling and cracking]": "[dunění a praskání]",
    "[screech]": "[skřek]",
    "[screeching]": "[skřeky]",
    "[thudding]": "[bušení]",
    "[floor crumbles]": "[podlaha se hroutí]",
    "[dying screech]": "[smrtelný skřek]",

    # === centce ===
    "[earpiece beeps]": "[pípnutí sluchátka]",
    "[generator rumbling]": "[hučení generátoru]",
    "[click]": "[cvaknutí]",
    "[helicopter blades whirring]": "[vrtání listů helikoptéry]",
    "[fastener rips]": "[trhání suchého zipu]",
    "[gun magazines click]": "[cvaknutí zásobníků]",
    "[blood splattering]": "[stříkání krve]",
    "[gunfire]": "[střelba]",
    "[gunshot]": "[výstřel]",
    "[rustling]": "[šustění]",
    "[cables groan and snap]": "[skřípání a praskání lan]",
    "[timer beeping]": "[pípání časovače]",
    "[explosion]": "[výbuch]",
    "[engine whirrs]": "[motor bzučí]",
    "[engine revs]": "[motor nabírá otáčky]",

    # === centhw ===
    "[rocket launcher blast]": "[výstřel z raketometu]",
    "[creatures snarling]": "[vrčení tvorů]",
    "[thwack]": "[prásknutí]",
    "[gasoline dripping]": "[kapání benzínu]",
    "[coughing]": "[kašlání]",
    "[flames spark]": "[jiskření plamenů]",
    "[screaming]": "[křik]",

    # === centrb ===
    "[engine stops]": "[motor se zastaví]",
    "[silence]": "[ticho]",
    "[monitor pings faintly]": "[slabé pípnutí monitoru]",
    "[ping]": "[pípnutí]",
    "[computer pings faintly]": "[slabé pípnutí počítače]",
    "[computer pings]": "[pípnutí počítače]",
    "[keyboard clicks]": "[klapání klávesnice]",
    "[Grace exhales]": "[Grace vydechne]",
    "[ragged breathing]": "[těžké dýchání]",
    "[gunshots]": "[výstřely]",
    "[huge crash]": "[obrovský náraz]",
    "[groans]": "[sténání]",
    "[ceiling crumbles]": "[strop se hroutí]",
    "[rumbling]": "[dunění]",
    "[rain pouring]": "[lijící déšť]",
    "[metal door squeaks]": "[skřípání kovových dveří]",
    "[large impact thud]": "[mohutný dopad]",
    "[missile whooshes through the air]": "[raketa hvízdá vzduchem]",
    "[heavy thud]": "[těžký úder]",
    "[muscles and sinew squelch]": "[mlaskání svalů a šlach]",
    "[blood spurts violently]": "[krev prudce stříká]",

    # === centuc ===
    "[loud creaking of metal]": "[hlasité vrzání kovu]",
    "[Plant 43 screams]": "[Plant 43 křičí]",
    "[gears turning, metal clanking]": "[otáčení ozubených kol, řinčení kovu]",
    "[door whirs shut]": "[dveře se se bzučením zavřou]",

    # === ending ===
    "[Nathan clearing his throat]": "[Nathan si odkašle]",
    "[radio static]": "[šum rádia]",

    # === ff2nd ===
    "[running footsteps]": "[běžící kroky]",
    "[glass shatters, researcher screams]": "[rozbíjení skla, křik výzkumníka]",
    "[banging]": "[bušení]",
    "[giggling]": "[chichotání]",
    "[flesh squelches]": "[mlaskání masa]",
    "[screaming in agony]": "[křik v agónii]",
    "[neck snaps]": "[zlomení vazu]",
    "[shaky breathing]": "[roztřesený dech]",
    "[Chloe gasps]": "[Chloe lapá po dechu]",
    "[coffin lids thump, Chloe screams]": "[bouchání víka rakve, Chloe křičí]",
    "[Chloe screams]": "[Chloe křičí]",
    "[metallic thudding]": "[kovové bušení]",
    "[panicked breathing]": "[panický dech]",
    "[clang]": "[řinčení]",
    "[projector humming]": "[bzučení projektoru]",

    # === hotel3 ===
    "[keyboard clicking]": "[klapání klávesnice]",
    "[mouse clicks]": "[klikání myší]",
    "[rapid knocking]": "[rychlé klepání]",
    "[grumbles]": "[bručení]",
    "[creaking]": "[vrzání]",
    "[door slams]": "[bouchnutí dveří]",
    "[gasps]": "[lapání po dechu]",
    "[frantic rustling]": "[zběsilé šustění]",
    "[thump]": "[bouchnutí]",
    "[door opens and shuts]": "[dveře se otevřou a zavřou]",
    "[Grace scoffs]": "[Grace si odfrkne]",
    "[phone ringing]": "[zvonění telefonu]",
    "[call disconnects]": "[hovor se přeruší]",
    "[loud click]": "[hlasité cvaknutí]",
    "[gun barrel clicks]": "[cvaknutí hlavně]",
    "[shuffling and gasping]": "[šoupání a lapání po dechu]",
    "[manager choking]": "[manažer se dusí]",
    "[body falls]": "[tělo padá]",
    "[hyperventilating]": "[hyperventilace]",
    "[gasping breaths]": "[ztěžklé dechy]",
    "[metal clinking]": "[cinkání kovu]",
    "[screaming in horror]": "[křik hrůzou]",
    "[blood spurting]": "[stříkání krve]",
    "[flames hiss and spread]": "[plameny syčí a šíří se]",
    "[wailing]": "[kvílení]",
    "[flames crackling]": "[praskání plamenů]",
    "[sniffling]": "[šmrkání]",
    "[ringing continues]": "[zvonění pokračuje]",
    "[SFX screech]": "[zvukový efekt skřeku]",
    "[pained choking]": "[bolestivé dušení]",
    "[blood splatters]": "[stříkání krve]",
    "[fabric straining]": "[napínání látky]",
    "[window shatters]": "[rozbití okna]",
    "[glass clattering]": "[cinkání skla]",
    "[groaning]": "[sténání]",
    "[♪ classical music]": "[♪ klasická hudba]",
    "[thunder]": "[hrom]",
    "[lock clicks]": "[cvaknutí zámku]",
    "[choking]": "[dušení]",
    "[chuckle]": "[uchechtnutí]",

    # === mange ===
    "[panting]": "[lapání po dechu]",
    "[restraints strain and clank]": "[napínání a řinčení pout]",
    "[blood drips]": "[kapání krve]",
    "[glass shatters]": "[rozbití skla]",
    "[sharp inhale]": "[ostrý nádech]",
    "[cry of pain]": "[bolestivý výkřik]",
    "[restraints clink]": "[cinkání pout]",
    "[Grace screams]": "[Grace křičí]",
    "[metal chains jangle]": "[řinčení kovových řetězů]",
    "[Grace gasps]": "[Grace lapá po dechu]",
    "[low growling]": "[tiché vrčení]",
    "[roaring]": "[řvaní]",
    "[thumping]": "[bušení]",
    "[panicking]": "[panika]",
    "[beep]": "[pípnutí]",
    "[roaring as flesh sizzles]": "[řev za prskání masa]",
    "[Grace screaming]": "[Grace křičí]",
    "[whimpering]": "[kňučení]",

    # === mangl ===
    "[lock beeps]": "[pípnutí zámku]",
    "[nervous breathing]": "[nervózní dýchání]",
    "[test tube clinks]": "[cinknutí zkumavky]",
    "[maniacal laughing]": "[šílený smích]",
    "[alarm blaring]": "[řev alarmu]",
    "[building crumbling]": "[hroutící se budova]",
    "[zombies groaning]": "[sténání zombií]",
    "[fence rattling]": "[chrastění plotu]",
    "[metallic twang]": "[kovové brnknutí]",
    "[switches flicking]": "[přepínání spínačů]",
    "[engine whirs to life]": "[motor naskočí]",
    "[Grace and Emily screaming]": "[Grace a Emily křičí]",
    "[Emily screaming]": "[Emily křičí]",
    "[alarm beeping]": "[pípání alarmu]",
    "[crashing]": "[bourání]",
    "[screams]": "[výkřiky]",

    # === mangm2 ===
    "[gasps]": "[lapání po dechu]",
    "[strap clicks open]": "[cvaknutí popruhu]",
    "[distant groaning]": "[vzdálené sténání]",
    "[murmur of agreement]": "[souhlasné mumlání]",
    "[loud crash]": "[silný náraz]",
    "[chains jangling]": "[řinčení řetězů]",
    "[deep breaths]": "[hluboké dechy]",

    # === mangm3 ===
    "[gasp]": "[prudký nádech]",
    "[monitor beeping]": "[pípání monitoru]",
    "[oozing]": "[prosakování]",
    "[receding footsteps]": "[vzdalující se kroky]",
    "[wristband clinks]": "[cinknutí náramku]",

    # === mangu ===
    "[flashlight clatters]": "[baterka zarachotí]",
    "[growling]": "[vrčení]",
    "[bars rattling]": "[chrastění mříží]",
    "[metallic clanking]": "[kovové řinčení]",
    "[elevator doors thumping]": "[bušení dveří výtahu]",
    "[scream]": "[výkřik]",
    "[cables snapping]": "[praskání lan]",
    "[sobbing]": "[vzlykání]",
    "[blood spurts and splatters]": "[krev stříká a cáká]",
    "[Grace crying]": "[Grace pláče]",

    # === mangua ===
    "[seatbelt clicks]": "[cvaknutí bezpečnostního pásu]",

    # === mangw ===
    "[pained whimpering]": "[bolestivé kňučení]",
    "[loud clanking]": "[hlasité řinčení]",
    "[hatch clanking open]": "[řinčivé otevírání poklopu]",
    "[hatch stops and power cuts]": "[poklop se zastaví a vypadne proud]",
    "[shrieks]": "[výkřiky]",
    "[melting]": "[tání]",
    "[door scrapes open]": "[dveře se se skřípáním otevřou]",
    "[counting compressions]": "[odpočítávání kompresí]",
    "[hand clanks against metal]": "[ruka narazí do kovu]",
    "[gasping scream]": "[udýchaný výkřik]",
    "[struggling screams]": "[křik při zápasu]",
    "[bubbling and cracking]": "[bublání a praskání]",
    "[fading screech]": "[slábnoucí skřek]",
    "[thunk]": "[žuchnutí]",
    "[wet cough]": "[vlhký kašel]",
    "[spits]": "[plivnutí]",
    "[chuckles]": "[smích]",
    "[shutter glides open]": "[roleta se otvírá]",
    "[metallic bang]": "[kovová rána]",

    # === manlc ===
    "[zombies growling]": "[vrčení zombií]",
    "[wet footsteps]": "[mokré kroky]",
    "[gurgling roar]": "[bublavý řev]",
    "[door creaks]": "[vrzání dveří]",
    "[eerie silence]": "[děsivé ticho]",
    "[crashes to a stop]": "[s rachotem zastaví]",
    "[Emily gasps painfully]": "[Emily bolestivě lapá po dechu]",
    "[zombies groaning]": "[sténání zombií]",

    # === manlh ===
    "[mechanical whirring]": "[mechanické bzučení]",
    "[door clicks shut]": "[cvaknutí zavíraných dveří]",
    "[thunder claps]": "[zahřmění]",
    "[intercom squeaks]": "[zaskřípání interkomu]",
    "[doctor groaning]": "[sténání doktora]",
    "[chainsaw revving]": "[naskakování řetězové pily]",
    "[pained groaning]": "[bolestivé sténání]",
    "[flesh splattering]": "[tříštění masa]",
    "[metallic grinding and slamming]": "[kovové skřípání a bouchání]",
    "[shutter closing]": "[zavírání rolety]",
    "[Leon groaning]": "[Leon sténá]",

    # === manlm ===
    "[light clicks on harshly]": "[ostré rozsvícení světla]",
    "[grunt]": "[zavrčení]",
    "[Leon grunts]": "[Leon zavrčí]",
    "[Leon clicks tongue]": "[Leon mlaskne]",
    "[Leon chuckles]": "[Leon se uchechtne]",
    "[deep breath]": "[hluboký nádech]",
    "[error alert]": "[chybové upozornění]",
    "[lock alert]": "[upozornění zámku]",
    "[beeping as text appears]": "[pípání při zobrazení textu]",

    # === movie ===
    "[♪ moody music]": "[♪ ponurá hudba]",
    "[hand claps]": "[tlesknutí]",
    "[pained moan]": "[bolestivý sten]",
    "[heavy breathing]": "[těžké dýchání]",
    "[yells]": "[křičí]",
    "[groan]": "[sten]",

    # === streetms ===
    "[police siren]": "[policejní siréna]",
    "[engine purrs to a start]": "[motor se s předením rozjede]",
    "[car horn blares]": "[troubení klaksonu]",
    "[muffled shot]": "[tlumený výstřel]",
    "[earpiece bleeps]": "[pípnutí sluchátka]",

    # === underco ===
    "[water dripping]": "[kapání vody]",
    "[sniffles]": "[popotahování]",
    "[grunting]": "[hekání]",
    "[metallic scraping]": "[kovové škrábání]",
    "[lock clicks open]": "[cvaknutí otevíraného zámku]",
    "[button clicks]": "[klikání tlačítek]",
    "[beeping]": "[pípání]",
    "[button click]": "[kliknutí tlačítka]",
    "[static]": "[šum]",
    "[metal straining, dirt trickling]": "[namáhání kovu, sypání hlíny]",
    "[grunts]": "[zavrčení]",
    "[coughs]": "[kašlání]",
    "[cane tapping]": "[klepání hole]",
    "[door clicks open]": "[cvaknutí otevíraných dveří]",
    "[Spencer chortles]": "[Spencer se chechtá]",
    "[door clicks shut]": "[cvaknutí zavíraných dveří]",
    "[sharp beeping]": "[ostré pípání]",
    "[wet coughing]": "[vlhký kašel]",
    "[soft groan]": "[tichý sten]",
    "[Leon coughing]": "[Leon kašle]",

    # === underhb ===
    "[heavy running footsteps]": "[těžké běžící kroky]",
    "[weapons twang]": "[brnknutí zbraní]",
    "[heavy clank]": "[těžké řinčení]",
    "[cough]": "[kašel]",
    "[skin cracking]": "[praskání kůže]",
    "[gasping]": "[lapání po dechu]",
    "[muscles squelch]": "[mlaskání svalů]",
    "[metal groaning]": "[skřípání kovu]",

    # === underlb ===
    "[depressurizing hiss]": "[syčení při odpuštění tlaku]",
    "[vial clinks]": "[cinknutí lahvičky]",
    "[Elpis dispensing]": "[Elpis se dávkuje]",
    "[Zeno grunts]": "[Zeno zavrčí]",
    "[bodies thud]": "[dopad těl]",
    "[Victor laughing]": "[Victor se směje]",
    "[Zeno chuckles]": "[Zeno se uchechtne]",
    "[Victor snarls]": "[Victor zavrčí]",
    "[Grace groaning]": "[Grace sténá]",
    "[metal groaning and collapsing]": "[skřípání a hroucení kovu]",
    "[Grace screaming]": "[Grace křičí]",
    "[structure falling]": "[padající konstrukce]",
    "[crazed yelling]": "[šílené řvaní]",
    "[body violently mutating]": "[tělo se prudce mutuje]",
    "[banging and crashing]": "[bušení a bourání]",
    "[dying scream]": "[smrtelný výkřik]",
    "[pained yell]": "[bolestivý výkřik]",
    "[spotlight clicks on loudly]": "[hlasité rozsvícení reflektoru]",
    "[rappelling noises]": "[zvuky slaňování]",
    "[facility crumbling]": "[hroutící se zařízení]",
    "[squelch as hatchet connects]": "[mlasknutí při zásahu sekerou]",
    "[facility collapsing]": "[kolaps zařízení]",
    "[elevator gears whirring]": "[bzučení ozubených kol výtahu]",

    # === enemy ===
    "[toy clacking]": "[klapání hračky]",
    "[Cole reloads shotgun]": "[Cole nabíjí brokovnici]",
    "[cart clattering]": "[rachotící vozík]",
    "[thumping overhead]": "[bušení nad hlavou]",
    "[wood cracking]": "[praskání dřeva]",
    "[creaking overhead]": "[vrzání nad hlavou]",
    "[loud crashing]": "[hlasitý náraz]",
    "[sniffing]": "[čenichání]",
    "[tense music]": "[napjatá hudba]",
    "[sound from duct]": "[zvuk z potrubí]",
    "[sound receding from duct]": "[zvuk se vzdaluje z potrubí]",
    "[chomping]": "[žvýkání]",
    "[anguished scream]": "[úzkostný výkřik]",
    "[heavy footsteps]": "[těžké kroky]",
    "[heavy footsteps in pursuit]": "[těžké kroky v pronásledování]",
    "[doorway breaking]": "[rozbíjení dveřního rámu]",
    "[sounds of struggle]": "[zvuky zápasu]",
    "[charging footsteps]": "[útočné kroky]",
    "[flesh and blood splattering]": "[stříkání masa a krve]",
    "[bones grinding]": "[drcení kostí]",
    "[pounding]": "[bušení]",
    "[crash into wall]": "[náraz do zdi]",
    "[walls breaking]": "[rozbíjení zdí]",
    "[wood breaking]": "[lámání dřeva]",
    "[loud cracking]": "[hlasité praskání]",
    "[falling thud]": "[dopad]",
    "[crazed roar]": "[šílený řev]",
    "[scuttling on outer walls]": "[cupitání po vnějších zdech]",
    "[giant spider screeches]": "[obří pavouk křičí]",
    "[wall cracking]": "[praskání zdi]",
    "[giant spider screeching]": "[křik obřího pavouka]",
    "[ladder snapping]": "[prasknutí žebříku]",
    "[wall crumbles]": "[zeď se hroutí]",
    "[giant spider hissing]": "[syčení obřího pavouka]",
    "[fading scuttling]": "[slábnoucí cupitání]",
    "[scuttling]": "[cupitání]",
    "[birthing squelch]": "[mlasknutí při porodu]",
    "[baby spiders scuttling]": "[cupitání malých pavouků]",
    "[baby spiders screeching]": "[křik malých pavouků]",
    "[guts splatter]": "[stříkání vnitřností]",
    "[door rattling]": "[chrastění dveří]",
    "[impact thud]": "[dopad]",
    "[wall breaking]": "[rozbíjení zdi]",
    "[violent crashing]": "[prudký náraz]",
    "[Tyrant roars]": "[Tyrant řve]",
    "[Tyrant groans]": "[Tyrant sténá]",
    "[metal crunches]": "[drcení kovu]",
    "[plant wilting]": "[vadnutí rostliny]",
    "[ground rumbles]": "[země se třese]",
    "[vines slithering away]": "[plazení úponků pryč]",
    "[violent tremors]": "[prudké otřesy]",
    "[thrashing]": "[zmítání]",
    "[footsteps]": "[kroky]",
    "[gas hissing]": "[syčení plynu]",
    "[licker screeching]": "[křik lickera]",
    "[slice]": "[seknutí]",
    "[licker reacting]": "[reakce lickera]",
    "[frenzied snarling]": "[zběsilé vrčení]",
    "[ominous music]": "[zlověstná hudba]",
    "[chainsaw clattering]": "[řinčení řetězové pily]",
    "[eerie singing]": "[děsivý zpěv]",
    "[violent scream]": "[prudký výkřik]",
    "[ears ringing]": "[pískání v uších]",
    "[scrubbing]": "[drhnutí]",
    "[corpse stirring]": "[mrtvola se pohne]",
    "[chopping]": "[sekání]",
    "[splash]": "[šplouchnutí]",
    "[large zombie roars]": "[velký zombie řve]",
    "[flesh squelching]": "[mlaskání masa]",
    "[war cry]": "[bojový pokřik]",
    "[chainsaw revving]": "[naskakování řetězové pily]",
    "[rapid gunfire]": "[rychlá střelba]",
    "[explosive beeping]": "[pípání výbušniny]",
    "[blood spurting]": "[stříkání krve]",

    # === level_centba ===
    "[wind whistling]": "[svištění větru]",
    "[metal creaking]": "[vrzání kovu]",
    "[snapping]": "[praskání]",

    # === level_centce ===
    "[loud blast]": "[hlasitý výbuch]",
    "[doors creaking open]": "[vrzavé otevírání dveří]",
    "[debris collapsing]": "[padající sutiny]",

    # === level_centhw ===
    "[large explosion]": "[velký výbuch]",
    "[building crumbles]": "[budova se hroutí]",

    # === level_centrb ===
    "[distant voices]": "[vzdálené hlasy]",
    "[metal straining]": "[namáhání kovu]",
    "[clattering]": "[rachotění]",

    # === level_centuc ===
    "[train creaking]": "[vrzání vlaku]",
    "[creaking intensifies]": "[vrzání se zesiluje]",
    "[crash]": "[náraz]",
    "[distant slithering]": "[vzdálené plazení]",
    "[container clicks open]": "[cvaknutí otevíraného kontejneru]",

    # === level_ff2nd ===
    "[man panicking]": "[muž v panice]",
    "[doorknob jiggling]": "[třesení klikou]",
    "[door opens]": "[dveře se otevřou]",
    "[ball rolling]": "[kutálení míče]",
    "[glass shatters, Chloe screams]": "[rozbití skla, Chloe křičí]",
    "[door shuts]": "[dveře se zavřou]",
    "[mechanism grinding]": "[skřípání mechanismu]",
    "[thumping from inside coffin]": "[bušení zevnitř rakve]",
    "[distant screaming]": "[vzdálený křik]",
    "[banging on glass]": "[bušení do skla]",
    "[shattering]": "[rozbíjení]",
    "[toy whirring and singing]": "[bzučení a zpívání hračky]",
    "[thunking]": "[bouchání]",
    "[Chloe crying]": "[Chloe pláče]",
    "[crazed screaming]": "[šílený křik]",
    "[crazed laughter]": "[šílený smích]",

    # === level_hotel3 ===
    "[train clanks by]": "[vlak projíždí s rachotem]",
    "[background chatter]": "[šum hovorů v pozadí]",
    "[distant police siren]": "[vzdálená policejní siréna]",
    "[flapping, Grace gasps]": "[plácání, Grace lapá po dechu]",
    "[small scream]": "[tichý výkřik]",
    "[disgusted gag]": "[zhnusené dávení]",
    "[insects buzzing]": "[bzučení hmyzu]",
    "[bucket rolls, Grace gasps]": "[kbelík se kutálí, Grace lapá po dechu]",
    "[footsteps overhead, Grace gasps]": "[kroky nad hlavou, Grace lapá po dechu]",
    "[distant door closing, Grace gasps]": "[vzdálené zavření dveří, Grace lapá po dechu]",
    "[deer head thuds]": "[jelení hlava bouchne]",
    "[distant thunder]": "[vzdálené hřmění]",
    "[Grace gasps]": "[Grace lapá po dechu]",
    "[glass shatters, Grace gasps]": "[rozbití skla, Grace lapá po dechu]",

    # === level_mange ===
    "[glass bottle clinking]": "[cinkání skleněné lahve]",
    "[distant intercom voice]": "[vzdálený hlas z interkomu]",
    "[a bang overhead, Grace gasps]": "[rána nad hlavou, Grace lapá po dechu]",
    "[metal tray clangs]": "[zvuk kovového tácu]",
    "[equipment clatters]": "[rachotění vybavení]",
    "[door smashes, Grace screams]": "[dveře se rozbijí, Grace křičí]",
    "[thunder claps, Grace gasps]": "[zahřmění, Grace lapá po dechu]",
    "[light shatters and Grace screams]": "[světlo se rozbije a Grace křičí]",

    # === level_mangl ===
    "[shuffling]": "[šouravé kroky]",
    "[glass pods shatter]": "[rozbití skleněných pouzder]",
    "[loud crashing]": "[hlasitý náraz]",
    "[mutation squelching]": "[mlaskání mutace]",
    "[object clattering]": "[rachotění předmětu]",

    # === level_mangm3 ===
    "[light switch clicking]": "[cvaknutí vypínače]",
    "[toilet flushing]": "[splachování záchodu]",
    "[distant singing]": "[vzdálený zpěv]",
    "[zombie screaming]": "[křik zombie]",
    "[engine rumbling]": "[hučení motoru]",
    "[piano note plays]": "[zaznění noty na piano]",
    "[child giggles]": "[dětský smích]",

    # === level_mangu ===
    "[distant zombies groaning]": "[vzdálené sténání zombií]",
    "[zombies banging on bars]": "[zombii buší do mříží]",
    "[lights clicking off]": "[cvakání zhasínajících světel]",
    "[blood pooling]": "[hromadění krve]",
    "[clanking]": "[řinčení]",
    "[loud crash, Emily and Grace scream]": "[silný náraz, Emily a Grace křičí]",
    "[grates clatter, Grace gasps]": "[mřížky rachotí, Grace lapá po dechu]",
    "[blood draining]": "[odtékání krve]",
    "[Emily and Grace screaming]": "[Emily a Grace křičí]",
    "[Grace yells]": "[Grace křičí]",
    "[electricity crackling]": "[praskání elektřiny]",

    # === level_mangua ===
    "[mechanical click]": "[mechanické cvaknutí]",
    "[crickets chirping]": "[cvrlikání cvrčků]",
    "[metallic sliding]": "[kovové klouzání]",

    # === level_mangw ===
    "[glass shatters]": "[rozbití skla]",
    "[banging on duct]": "[bušení do potrubí]",
    "[duct cover clattering]": "[rachotění krytu potrubí]",
    "[water flowing]": "[tekoucí voda]",
    "[floodlight clicks off]": "[zhasnutí reflektoru]",
    "[electricity activating]": "[spuštění elektřiny]",
    "[power clicking on]": "[zapnutí napájení]",
    "[Emily whimpering]": "[Emily kňučí]",
    "[power cuts]": "[výpadek proudu]",
    "[clambering]": "[šplhání]",

    # === level_manlc ===
    "[distant explosion]": "[vzdálený výbuch]",
    "[debris falling]": "[padající trosky]",

    # === level_manlh ===
    "[zombies groaning and banging on door]": "[sténání zombií a bušení do dveří]",
    "[shutter clanking open]": "[řinčivé otevírání rolety]",

    # === level_manlm ===
    "[wall crumbling]": "[hroutící se zeď]",
    "[mechanism opening]": "[otevírání mechanismu]",
    "[mechanism stopping]": "[zastavení mechanismu]",
    "[blinds breaking]": "[lámání žaluzií]",
    "[elevator stopping]": "[zastavení výtahu]",

    # === level_streetms ===
    "[pedestrians screaming]": "[křik chodců]",
    "[cars honking and crashing]": "[troubení a nabourávání aut]",
    "[woman screaming]": "[křik ženy]",

    # === level_underco ===
    "[glass cracking]": "[praskání skla]",
    "[door whirs open]": "[dveře se se bzučením otevřou]",
    "[creatures screeching]": "[křik tvorů]",
    "[pods whirring]": "[bzučení pouzder]",
    "[movement from the duct]": "[pohyb z potrubí]",
    "[elevator doors ding]": "[cinknutí dveří výtahu]",
    "[heart pounding fast]": "[rychlý tlukot srdce]",

    # === level_underhb ===
    "[doors open]": "[dveře se otevřou]",

    # === level_underlb ===
    "[generator exploding]": "[exploze generátoru]",
    "[generator explodes]": "[generátor exploduje]",
}


def translate_file(filename):
    """Process a single soundsupport file and generate translation."""
    src_path = os.path.join(SRC_DIR, filename)
    out_path = os.path.join(OUT_DIR, filename)

    with open(src_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    entries = data.get('entries', [])
    result = {}

    for entry in entries:
        name = entry.get('name', '')
        strings = entry.get('strings', {})
        en_text = strings.get('en', '')

        if en_text.strip():
            # Look up translation
            if en_text in TRANSLATIONS:
                result[name] = TRANSLATIONS[en_text]
            else:
                # Report missing translation
                print(f"  WARNING: No translation for: {repr(en_text)} in {filename}")
                result[name] = en_text  # Keep original as fallback
        else:
            # Empty English text -> keep empty
            result[name] = ""

    if result:
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        en_count = sum(1 for v in result.values() if v)
        empty_count = sum(1 for v in result.values() if not v)
        print(f"  Created: {out_path} ({en_count} translated, {empty_count} empty)")
    else:
        print(f"  Skipped (no entries): {filename}")


def main():
    files = sorted(os.listdir(SRC_DIR))
    print(f"Found {len(files)} soundsupport files to translate.\n")

    for filename in files:
        if not filename.endswith('.json'):
            continue
        print(f"Processing: {filename}")
        translate_file(filename)

    print(f"\nDone. Translations written to: {OUT_DIR}")


if __name__ == "__main__":
    main()
