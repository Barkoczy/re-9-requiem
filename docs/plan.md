# Plán auditu překladu (2026-02-27)

## Cíl
Provést plný audit 122 překladových JSON souborů a opravit prokazatelné odchylky od pravidel (`README.md`, `docs/pravidla-prekladu.md`, `docs/architektura.md`) se zaměřením na:
- nepřekládané názvy (postavy, místa, zbraně, organizace),
- konzistenci terminologie,
- technickou integritu textů (tagy, placeholdery, uvozovky, linebreaky).

## Postup
- [x] Načíst a potvrdit závazná pravidla a architekturu.
- [x] Spustit strojový audit všech souborů proti `json/` originálu.
- [x] Vyhodnotit nálezy podle rizika (kritické / střední / kosmetické).
- [x] Aplikovat pouze bezpečné a jednoznačné opravy (konkrétní regresní chyby).
- [x] Znovu spustit audit a zkontrolovat nulovou regresi u opravených výrazů.
- [x] Dodat souhrn změn + příkazy pro ověření.

## Kritéria bezpečné opravy
- Oprava nesmí měnit klíče JSON.
- Oprava nesmí porušit tagy (`<ICON>`, `<REF>`, `<COLOR ...>`), formátovací tokeny (`{0}`, `%d`, `%s`) ani linebreaky (`\r\n`, `\n`).
- Oprava musí být v souladu s terminologickým slovníkem.
- Nejprve opravovat jen nálezy s vysokou jistotou (např. zjevné duplicity textu, špatný pád po automatické náhradě).

## Rozhodnutí z validace komunity
- `Leone`, pádové tvary `T-Virus` a jména `Zeno`, `Alyssa` jsou schválené pro tento projekt.
- U zbraní platí kontext: názvy itemů EN, ale v dialogu přirozený CZ žargon (např. `sekyrka`, `samopal`).

## Rollback
- V případě regresí vrátit pouze dotčené soubory přes `git restore --source=HEAD -- <soubor>` pro konkrétní cesty.
