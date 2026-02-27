# Plán auditu překladu (2026-02-27)

## Cíl
Provést plný audit 122 překladových JSON souborů a opravit prokazatelné odchylky od pravidel (`README.md`, `docs/pravidla-prekladu.md`, `docs/architektura.md`) se zaměřením na:
- nepřekládané názvy (postavy, místa, zbraně, organizace),
- konzistenci terminologie,
- technickou integritu textů (tagy, placeholdery, uvozovky, linebreaky).

## Postup
- [x] Načíst a potvrdit závazná pravidla a architekturu.
- [ ] Spustit strojový audit všech souborů proti `json/` originálu.
- [ ] Vyhodnotit nálezy podle rizika (kritické / střední / kosmetické).
- [ ] Aplikovat pouze bezpečné a jednoznačné opravy.
- [ ] Znovu spustit audit a zkontrolovat nulovou regresi.
- [ ] Dodat souhrn změn + příkazy pro ověření.

## Kritéria bezpečné opravy
- Oprava nesmí měnit klíče JSON.
- Oprava nesmí porušit tagy (`<ICON>`, `<REF>`, `<COLOR ...>`), formátovací tokeny (`{0}`, `%d`, `%s`) ani linebreaky (`\r\n`, `\n`).
- Oprava musí být v souladu s terminologickým slovníkem.
- Nejprve opravovat jen nálezy s vysokou jistotou (např. zjevné počeštění jmen typu `Leone`).

## Rollback
- V případě regresí vrátit pouze dotčené soubory přes `git restore --source=HEAD -- <soubor>` pro konkrétní cesty.
