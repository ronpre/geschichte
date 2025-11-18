from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

BASE_PATH = Path(__file__).resolve().parent
HISTORY_LOG_PATH = BASE_PATH / "history_log.json"
HISTORY_RECENT_WINDOW = 30
HISTORY_MAX_ENTRIES = 180

MONTHS = {
    1: "Januar",
    2: "Februar",
    3: "Maerz",
    4: "April",
    5: "Mai",
    6: "Juni",
    7: "Juli",
    8: "August",
    9: "September",
    10: "Oktober",
    11: "November",
    12: "Dezember",
}

UPDATE_TIME = "09:00"

CATEGORY_ORDER = [
    "politik",
    "wirtschaft",
    "zeitgeschichte",
    "gesellschaft",
    "antike",
]

ARTICLES = {
    "politik": [
        {
            "slug": "politik-1648",
            "title": "Politik: Westfaelischer Frieden 1648",
            "paragraphs": [
                "<strong>Ereignis:</strong> Am 24. Oktober 1648 beendeten die Vertraege von Muenster und Osnabrueck den Dreissigjaehrigen Krieg, erkannten die Souveraenitaet der Reichsstaende an und verschoben das Machtgleichgewicht zugunsten Frankreichs und Schwedens.",
                "<strong>Folgen:</strong> Die Vereinbarungen etablierten eine europaweite Diplomatie mit regelmaessigen Kongressen, gaben kleineren Staaten mehr Verhandlungsspielraum und verankerten die Idee, dass religioese Konflikte politisch vermittelt werden koennen.",
                "<strong>Was wir gelernt haben:</strong> Dauerhafte Friedensordnungen benoetigen geteilte Sicherheitsgarantien, klare Grenzregelungen und Foren fuer Konfliktbearbeitung, damit Sieger und Besiegte langfristig kooperieren.",
                "<strong>Vertiefung:</strong> Westfaelische Instrumente wie Gesandtenkongresse und Protokollregeln praegen bis heute zwischenstaatliche Verhandlungen und legten die Grundlage fuer moderne Voelkerrechtsprinzipien.",
            ],
            "source_label": "Encyclopaedia Britannica",
            "source_title": "Peace of Westphalia",
            "source_url": "https://www.britannica.com/event/Peace-of-Westphalia",
        },
        {
            "slug": "politik-1947",
            "title": "Politik: Unabhaengigkeit Indiens 1947",
            "paragraphs": [
                "<strong>Ereignis:</strong> Am 15. August 1947 entliess Grossbritannien das ehemalige Britisch-Indien in die Unabhaengigkeit, wodurch die Dominions Indien und Pakistan entstanden und eine massive Migrationsbewegung ausgeloest wurde.",
                "<strong>Folgen:</strong> Die Teilung schuf neue Verfassungsprozesse, stellte Verwaltungsstrukturen auf die Probe und machte Grenzfragen wie Kaschmir zum zentralen Konfliktfeld zwischen den Nachbarstaaten.",
                "<strong>Was wir gelernt haben:</strong> Dekolonisation gelingt nachhaltiger, wenn Minderheitenschutz, gemeinsame Institutionen und wirtschaftliche Verflechtungen parallel aufgebaut werden.",
                "<strong>Vertiefung:</strong> Die indische Verfassung von 1950 kombinierte parlamentarische Demokratie, Foederalismus und Grundrechte und wurde zum Referenzrahmen fuer viele Staaten des Globalen Suedens.",
            ],
            "source_label": "Library of Congress",
            "source_title": "Independence for the Indian Subcontinent",
            "source_url": "https://www.loc.gov/exhibits/british-empire/independence-for-indian-subcontinent.html",
        },
        {
            "slug": "politik-1975",
            "title": "Politik: Helsinki-Schlussakte 1975",
            "paragraphs": [
                "<strong>Ereignis:</strong> Am 1. August 1975 unterzeichneten 35 Staaten der KSZE in Helsinki eine Schlussakte, die Grenzen in Europa anerkannte, Menschenrechte hervorhob und vertrauensbildende Sicherheitsmassnahmen vereinbarte.",
                "<strong>Folgen:</strong> Die Konferenz schuf Berichtspflichten, Beobachterformate und neue Kommunikationskanaele zwischen Ost und West, was Buergerrechtsbewegungen in Osteuropa zusaetzlich staerkte.",
                "<strong>Was wir gelernt haben:</strong> Dialogplattformen koennen selbst unter Systemkonflikten funktionieren, wenn sie Transparenzanforderungen, militaerische Vertrauensmassnahmen und Zivilgesellschaftsrechte verbinden.",
                "<strong>Vertiefung:</strong> Die OSZE uebernimmt bis heute Wahlbeobachtungen, Konfliktpraevention und Mediationen, die direkt aus den Helsinki-Standards abgeleitet sind.",
            ],
            "source_label": "OSZE",
            "source_title": "Helsinki Final Act",
            "source_url": "https://www.osce.org/helsinki-final-act",
        },
        {
            "slug": "politik-1998",
            "title": "Politik: Good-Friday-Agreement 1998",
            "paragraphs": [
                "<strong>Ereignis:</strong> Am 10. April 1998 legte das Karfreitagsabkommen den Grundstein fuer eine Machtteilung in Nordirland, beendete den bewaffneten Konflikt weitgehend und schuf neue grenzueberschreitende Institutionen.",
                "<strong>Folgen:</strong> Gewaltakte nahmen drastisch ab, die Polizeireform begann und kulturelle Identitaeten erhielten gleichberechtigtere Anerkennung innerhalb eines gemeinsamen politischen Rahmens.",
                "<strong>Was wir gelernt haben:</strong> Friedensabkommen muessen Sicherheitsgarantien, politische Teilhabe und soziooekonomische Entwicklungsprogramme kombinieren, um bewaffnete Gruppen langfristig zu integrieren.",
                "<strong>Vertiefung:</strong> Die Einrichtung gemeinsamer Ministerien und Foren zwischen Belfast, Dublin und London dient international als Blaupause fuer postkonfliktuelle Machtteilung.",
            ],
            "source_label": "UK Government",
            "source_title": "The Belfast Agreement",
            "source_url": "https://www.gov.uk/government/publications/the-belfast-agreement",
        },
    ],
    "wirtschaft": [
        {
            "slug": "wirtschaft-1944",
            "title": "Wirtschaft: Bretton-Woods-System 1944",
            "paragraphs": [
                "<strong>Ereignis:</strong> Im Juli 1944 schufen 44 Staaten in Bretton Woods ein System fester Wechselkurse, gruendeten den Internationalen Waehrungsfonds und die Weltbank und banden den US-Dollar an Gold.",
                "<strong>Folgen:</strong> Gemeinsame Regeln fuer Kapitalverkehr, Kreditlinien und Zahlungsbilanzen beschleunigten den Wiederaufbau und liessen den Welthandel bis in die 1960er Jahre stark wachsen.",
                "<strong>Was wir gelernt haben:</strong> Globale Finanzarchitekturen benoetigen Anpassungsmechanismen und transparente Aufsicht, um Ungleichgewichte fruehzeitig zu korrigieren.",
                "<strong>Vertiefung:</strong> Nachfolgeinstrumente des IWF, etwa Sonderziehungsrechte, greifen weiterhin auf Grundideen von Bretton Woods zurueck.",
            ],
            "source_label": "International Monetary Fund",
            "source_title": "The Enduring Legacy of Bretton Woods",
            "source_url": "https://www.imf.org/external/about/histcoop.htm",
        },
        {
            "slug": "wirtschaft-1947",
            "title": "Wirtschaft: Marshallplan 1947",
            "paragraphs": [
                "<strong>Ereignis:</strong> Im April 1948 startete das European Recovery Program, besser bekannt als Marshallplan, mit dem die USA Milliarden fuer den Wiederaufbau Westeuropas bereitstellten.",
                "<strong>Folgen:</strong> Kredite, Rohstofflieferungen und Technologietransfer staerkten Industrieproduktion, fuehrten zu neuen Handelspartnerschaften und verankerten transatlantische Kooperation.",
                "<strong>Was wir gelernt haben:</strong> Wiederaufbauprogramme wirken nachhaltiger, wenn sie wirtschaftliche Integration, Produktivitaetssteigerungen und Bildungsoffensiven verbinden.",
                "<strong>Vertiefung:</strong> Die Organisation fuer Europaesche Wirtschaftliche Zusammenarbeit, Vorlaeufer der OECD, koordinierte die Mittelverwendung und wurde zu einem Forum fuer gemeinsame Planung.",
            ],
            "source_label": "US Department of State",
            "source_title": "The Marshall Plan",
            "source_url": "https://www.state.gov/the-marshall-plan/",
        },
        {
            "slug": "wirtschaft-1999",
            "title": "Wirtschaft: Euro-Einfuehrung 1999",
            "paragraphs": [
                "<strong>Ereignis:</strong> Am 1. Januar 1999 fuehrten elf EU-Staaten den Euro als Buchwaehrung ein und uebertrugen die Geldpolitik an die neu gegruendete Europaeische Zentralbank.",
                "<strong>Folgen:</strong> Der gemeinsame Waehrungsraum erleichterte Handel, senkte Transaktionskosten und machte fiskalische Koordinierung sowie Stabilitaetspakte zwingend.",
                "<strong>Was wir gelernt haben:</strong> Gemeinsame Waehrungen erfordern strenge Haushaltsueberwachung, Bankenaufsicht und geteilte Kriseninstrumente, um asymmetrische Schocks aufzufangen.",
                "<strong>Vertiefung:</strong> Die Kapitalmarktunion, Rettungsschirme und die Bankenunion bauen auf den institutionellen Strukturen der Euro-Einfuehrung auf.",
            ],
            "source_label": "Europaeische Zentralbank",
            "source_title": "Introduction of the Euro",
            "source_url": "https://www.ecb.europa.eu/euro/intro/html/index.en.html",
        },
        {
            "slug": "wirtschaft-2001",
            "title": "Wirtschaft: WTO-Beitritt Chinas 2001",
            "paragraphs": [
                "<strong>Ereignis:</strong> Am 11. Dezember 2001 trat China der Welthandelsorganisation bei und verpflichtete sich zu Zollsenkungen, Marktliberalisierung und Rechtsreformen im Handel.",
                "<strong>Folgen:</strong> Die Integration Chinas in den Welthandel senkte Konsumpreise weltweit, verstaerkte jedoch Wettbewerbsdruck auf Industriearbeitnehmer in vielen Regionen.",
                "<strong>Was wir gelernt haben:</strong> Handelserweiterungen brauchen flankierende Sozial- und Strukturpolitik, damit Produktivitaetsgewinne breiter verteilt werden.",
                "<strong>Vertiefung:</strong> Debatten ueber Lieferketten, Technologietransfer und faire Marktbedingungen praegen seither die internationale Wirtschaftspolitik.",
            ],
            "source_label": "World Trade Organization",
            "source_title": "China and the WTO",
            "source_url": "https://www.wto.org/english/thewto_e/acc_e/a1_china_e.htm",
        },
    ],
    "zeitgeschichte": [
        {
            "slug": "zeitgeschichte-1989",
            "title": "Zeitgeschichte: Fall der Berliner Mauer 1989",
            "paragraphs": [
                "<strong>Ereignis:</strong> Am 9. November 1989 oeffnete die Berliner Mauer nach einer missverstandenen Pressekonferenz, was spontane Grenzuebergaenge, Jubel und den raschen Zusammenbruch der DDR-Grenzinfrastruktur ausloeste.",
                "<strong>Folgen:</strong> Familien wurden wiedervereint, kommunistische Regime in Osteuropa gerieten unter Reformdruck und die deutsche Einigung wurde binnen eines Jahres politisch umgesetzt.",
                "<strong>Was wir gelernt haben:</strong> Kommunikation in Krisenzeiten kann kipppunktartig wirken; Transparenz und vorbereitete Fahrplaene sind entscheidend, um friedliche Umbrueche zu begleiten.",
                "<strong>Vertiefung:</strong> Erinnerungsorte, Bildungsprogramme und Forschungsstaetten analysieren seither die Ursachen friedlicher Revolutionen und deren Bedeutung fuer heutige Transformationsprozesse.",
            ],
            "source_label": "Encyclopaedia Britannica",
            "source_title": "Fall of the Berlin Wall",
            "source_url": "https://www.britannica.com/event/fall-of-the-Berlin-Wall",
        },
        {
            "slug": "zeitgeschichte-1986",
            "title": "Zeitgeschichte: Reaktorkatastrophe von Tschernobyl 1986",
            "paragraphs": [
                "<strong>Ereignis:</strong> Am 26. April 1986 explodierte Block 4 des Kernkraftwerks Tschernobyl, verbreitete radioaktive Wolken ueber Europa und machte weite Gebiete um Pripjat unbewohnbar.",
                "<strong>Folgen:</strong> Evakuierungen, Langzeitkrankheiten und enorme Dekontaminationskosten veraenderten die Energiedebatte weltweit und fuehrten zu strengeren Sicherheitsstandards.",
                "<strong>Was wir gelernt haben:</strong> Hochrisikotechnologien brauchen transparente Aufsicht, Notfallplaene und eine Sicherheitskultur, die Fehler offenlegt, statt sie zu vertuschen.",
                "<strong>Vertiefung:</strong> Internationale Agenturen wie die IAEA koordinieren seither Stresstests, Informationsaustausch und Sicherheitsmissionen fuer Atomkraftwerke.",
            ],
            "source_label": "International Atomic Energy Agency",
            "source_title": "Chernobyl Accident",
            "source_url": "https://www.iaea.org/topics/chernobyl",
        },
        {
            "slug": "zeitgeschichte-1995",
            "title": "Zeitgeschichte: Wahrheitskommission Suedafrika 1995",
            "paragraphs": [
                "<strong>Ereignis:</strong> 1995 setzte Suedafrika die Truth and Reconciliation Commission ein, um Verbrechen der Apartheid aufzuklaeren, Opfern Gehoer zu geben und ueber Amnestien zu entscheiden.",
                "<strong>Folgen:</strong> Oeffentliche Anhoerungen, Reparationsempfehlungen und nationale Debatten unterstuetzten den Uebergang zu einer inklusiveren Demokratie trotz ungeloster Ungleichheiten.",
                "<strong>Was wir gelernt haben:</strong> Versoehnungspolitik verlangt Kombinationen aus Wahrheit, Verantwortlichkeit und Reformprogrammen, damit Vertrauen zwischen Gesellschaftsgruppen entstehen kann.",
                "<strong>Vertiefung:</strong> Viele Laender uebersetzten das Modell in eigene Wahrheitskommissionen und kombinierten es mit Strafverfolgung sowie Restitutionsmassnahmen.",
            ],
            "source_label": "South African Government",
            "source_title": "Truth and Reconciliation Commission Reports",
            "source_url": "https://www.justice.gov.za/trc/report/",
        },
        {
            "slug": "zeitgeschichte-2011",
            "title": "Zeitgeschichte: Arabischer Fruehling 2011",
            "paragraphs": [
                "<strong>Ereignis:</strong> Ausgehend von Protesten in Tunesien Ende 2010 breitete sich 2011 eine Welle von Demonstrationen und Aufstaenden in der arabischen Welt aus, die Autoritarismus und soziale Ungleichheit infrage stellten.",
                "<strong>Folgen:</strong> Manche Staaten sahen Reformen oder Regierungswechsel, andere gerieten in langwierige Konflikte; regionale und internationale Akteure rangen um Einfluss.",
                "<strong>Was wir gelernt haben:</strong> Soziale Medien, demografischer Druck und wirtschaftliche Perspektivlosigkeit koennen politische Systeme schnell destabilisieren, wenn Reformkanaele fehlen.",
                "<strong>Vertiefung:</strong> Analysen untersuchen weiterhin, welche institutionellen Faktoren den Transformationsverlauf bestimmten und wie Resilienz autoritaerer Regime funktioniert.",
            ],
            "source_label": "Council on Foreign Relations",
            "source_title": "The Arab Spring at Ten",
            "source_url": "https://www.cfr.org/timeline/arab-spring",
        },
    ],
    "gesellschaft": [
        {
            "slug": "gesellschaft-1964",
            "title": "Gesellschaft: Civil Rights Act 1964",
            "paragraphs": [
                "<strong>Ereignis:</strong> Am 2. Juli 1964 unterzeichnete US-Praesident Lyndon B. Johnson den Civil Rights Act, der Rassentrennung im oeffentlichen Leben verbot und den Zugang zu Wahlrechten schuetze.",
                "<strong>Folgen:</strong> Gerichte, Bundesbehoerden und Aktivistinnen konnten diskriminierende Praktiken konsequenter anfechten; das Gesetz wirkte als Motor fuer weitere Gleichberechtigungsagenda.",
                "<strong>Was wir gelernt haben:</strong> Gesetzliche Gleichstellung muss mit Durchsetzungsmechanismen, Bildungsinvestitionen und gesellschaftlichem Dialog flankiert werden, damit sie Wirkung entfaltet.",
                "<strong>Vertiefung:</strong> Der Civil Rights Act bildet eine Grundlage fuer spaetere Antidiskriminierungsnormen, etwa im Bereich Behinderung, Geschlecht oder Herkunft.",
            ],
            "source_label": "National Archives",
            "source_title": "The Civil Rights Act",
            "source_url": "https://www.archives.gov/milestone-documents/civil-rights-act",
        },
        {
            "slug": "gesellschaft-1971",
            "title": "Gesellschaft: Frauenstimmrecht Schweiz 1971",
            "paragraphs": [
                "<strong>Ereignis:</strong> In einer Volksabstimmung am 7. Februar 1971 sprach sich die Schweiz fuer das Frauenstimmrecht auf Bundesebene aus und schloss damit eine lange Phase der politischen Ausschliessung.",
                "<strong>Folgen:</strong> Frauen konnten nun an nationalen Wahlen teilnehmen, Mandate uebernehmen und Gleichstellungsfragen staerker auf die politische Agenda setzen.",
                "<strong>Was wir gelernt haben:</strong> Inklusivere Demokratien entstehen durch hartnaeckige Zivilgesellschaft, Allianzen ueber Parteigrenzen hinweg und durch die Argumentation, dass Teilhabe Demokratie stabilisiert.",
                "<strong>Vertiefung:</strong> Kantone passten sukzessive ihre Gesetze an, waehrend Bildungsinitiativen politische Partizipation von Frauen weiter foerderten.",
            ],
            "source_label": "swissinfo",
            "source_title": "Women gain the vote in Switzerland",
            "source_url": "https://www.swissinfo.ch/eng/politics/womens-vote-50-years/46377464",
        },
        {
            "slug": "gesellschaft-1991",
            "title": "Gesellschaft: World Wide Web 1991",
            "paragraphs": [
                "<strong>Ereignis:</strong> Am 6. August 1991 stellte das CERN das World Wide Web der Oeffentlichkeit zur Verfuegung, wodurch Hypertext-Dokumente weltweit ueber das Internet abrufbar wurden.",
                "<strong>Folgen:</strong> Forschung, Medien, Handel und Bildung verlagerten Inhalte ins Netz; neue Branchen und digitale Kommunikationsformen entstanden in kurzer Zeit.",
                "<strong>Was wir gelernt haben:</strong> Offene Standards und lizenzfreie Technologien beschleunigen Innovation, muessen aber von Datenschutz- und Ethikregeln begleitet werden.",
                "<strong>Vertiefung:</strong> Das Web-Konsortium setzt bis heute technische Spezifikationen fest, waehrend Debatten um digitale Souveraenitaet und Plattformregulierung an Bedeutung gewinnen.",
            ],
            "source_label": "CERN",
            "source_title": "The Birth of the Web",
            "source_url": "https://home.cern/science/computing/birth-web",
        },
        {
            "slug": "gesellschaft-2006",
            "title": "Gesellschaft: UN-Behindertenrechtskonvention 2006",
            "paragraphs": [
                "<strong>Ereignis:</strong> Die UN-Generalversammlung verabschiedete am 13. Dezember 2006 die Konvention ueber die Rechte von Menschen mit Behinderungen, die 2008 in Kraft trat.",
                "<strong>Folgen:</strong> Staaten verpflichteten sich zu Barrierefreiheit, Inklusion im Bildungssystem und rechtlicher Gleichstellung; Monitoringstellen ueberwachen Fortschritte und Defizite.",
                "<strong>Was wir gelernt haben:</strong> Menschenrechte muessen intersektional gedacht werden, damit strukturelle Diskriminierung in Arbeit, Wohnen und politischer Teilhabe abgebaut wird.",
                "<strong>Vertiefung:</strong> Nationale Aktionsplaene, Aktionsforschung und Selbstvertretungsorganisationen treiben seitdem Reformen fuer inklusive Gesellschaften voran.",
            ],
            "source_label": "Vereinte Nationen",
            "source_title": "Convention on the Rights of Persons with Disabilities",
            "source_url": "https://www.un.org/development/desa/disabilities/convention-on-the-rights-of-persons-with-disabilities.html",
        },
    ],
    "antike": [
        {
            "slug": "antike-1750",
            "title": "Antike: Kodex Hammurabi ca. 1750 v. Chr.",
            "paragraphs": [
                "<strong>Ereignis:</strong> Um 1750 v. Chr. liess Koenig Hammurabi von Babylon einen umfangreichen Gesetzeskorpus in Stein meisseln, der Eigentums-, Familien- und Strafrecht regelte.",
                "<strong>Folgen:</strong> Der Kodex schuf Rechtssicherheit fuer Handel und Verwaltung, legitimierte monarchische Autoritaet und diente als Vorlage fuer spaetere Keilschriftgesetzgebungen.",
                "<strong>Was wir gelernt haben:</strong> Schriftliche Gesetze erhoehen Transparenz, muessen aber regelmaessig angepasst werden, damit soziale Gruppen nicht benachteiligt werden.",
                "<strong>Vertiefung:</strong> Der Kodex zeigt fruehe Abstufungen von Strafen nach sozialem Status und inspiriert Forschungen zu Gerechtigkeitsvorstellungen im Alten Orient.",
            ],
            "source_label": "Encyclopaedia Britannica",
            "source_title": "Code of Hammurabi",
            "source_url": "https://www.britannica.com/topic/Code-of-Hammurabi",
        },
        {
            "slug": "antike-0300",
            "title": "Antike: Bibliothek von Alexandria 3. Jh. v. Chr.",
            "paragraphs": [
                "<strong>Ereignis:</strong> Im 3. Jahrhundert v. Chr. gruendete das ptolemaeische Herrscherhaus in Alexandria eine Bibliothek, die Aufbewahrung und Uebersetzung antiker Texte zum Ziel hatte.",
                "<strong>Folgen:</strong> Gelehrte aus vielen Regionen tauschten Wissen aus, katalogisierten Schriften und entwickelten philologische Methoden, die Wissenschaften bis heute praegen.",
                "<strong>Was wir gelernt haben:</strong> Wissenszentren gedeihen durch offene Sammlungen, Sprachkompetenz und staatliche Foerderung, bleiben jedoch an politische Stabilitaet gebunden.",
                "<strong>Vertiefung:</strong> Rekonstruktionen der Bibliothek zeigen, wie antike Infrastruktur und Stiftungen globale Wissensnetzwerke ermoeglichten.",
            ],
            "source_label": "Encyclopaedia Britannica",
            "source_title": "Library of Alexandria",
            "source_url": "https://www.britannica.com/place/Library-of-Alexandria",
        },
        {
            "slug": "antike-0594",
            "title": "Antike: Reformen des Solon 594 v. Chr.",
            "paragraphs": [
                "<strong>Ereignis:</strong> 594 v. Chr. uebernahm Solon in Athen weitreichende Vollmachten, hob Schuldknechtschaft auf und reorganisierte politische Beteiligung nach Einkommensklassen.",
                "<strong>Folgen:</strong> Die Reformen stabilisierten Athen, weiteten Mitbestimmung aus und legten Grundlagen fuer spaetere demokratische Institutionen wie Rat und Volksgericht.",
                "<strong>Was wir gelernt haben:</strong> Soziale Spannungen lassen sich durch ausgewogene Kombinationen von Schuldenerlass, Rechtsreform und politischer Inklusion entspannen.",
                "<strong>Vertiefung:</strong> Spaetere Gesetzgeber wie Kleisthenes knuepften an Solons Kompromisse an und entwickelten die attische Demokratie weiter.",
            ],
            "source_label": "Encyclopaedia Britannica",
            "source_title": "Solon",
            "source_url": "https://www.britannica.com/biography/Solon",
        },
        {
            "slug": "antike-0312",
            "title": "Antike: Via Appia 312 v. Chr.",
            "paragraphs": [
                "<strong>Ereignis:</strong> 312 v. Chr. begann Rom den Bau der Via Appia, einer befestigten Fernstrasse, die die Hauptstadt mit Sueditalien verband und Truppentransporte beschleunigte.",
                "<strong>Folgen:</strong> Die Strasse erleichterte Handel, Verwaltung und kulturellen Austausch und wurde zum Vorbild fuer das roemische Strassennetz.",
                "<strong>Was wir gelernt haben:</strong> Infrastrukturprojekte koennen Machtprojektion, Wirtschaft und Integration gleichzeitig staerken, wenn Wartung und Sicherheit gewaehrleistet sind.",
                "<strong>Vertiefung:</strong> Archaeologische Untersuchungen zeigen, wie Ingenieurkunst, Vermessung und lokale Arbeitskraefte zusammenspielten, um dauerhafte Verkehrswege zu schaffen.",
            ],
            "source_label": "Encyclopaedia Britannica",
            "source_title": "Appian Way",
            "source_url": "https://www.britannica.com/topic/Appian-Way",
        },
    ],
}


def german_long_date(dt: datetime) -> str:
    return f"{dt.day}. {MONTHS[dt.month]} {dt.year}"


def german_short_date(dt: datetime) -> str:
    return f"{dt.day}.{dt.month:02d}.{str(dt.year)[-2:]}"

def load_history(path: Path = HISTORY_LOG_PATH) -> dict[str, list[dict[str, object]]]:
    if not path.exists():
        return {"history": []}

    try:
        raw_data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError, UnicodeDecodeError):
        return {"history": []}

    entries = raw_data.get("history")
    if not isinstance(entries, list):
        return {"history": []}

    cleaned: list[dict[str, object]] = []
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        date_value = entry.get("date")
        slugs_value = entry.get("slugs")
        if isinstance(date_value, str) and isinstance(slugs_value, list):
            valid_slugs = [slug for slug in slugs_value if isinstance(slug, str)]
            cleaned.append({"date": date_value, "slugs": valid_slugs})
    return {"history": cleaned}


def save_history(history: dict[str, list[dict[str, object]]], path: Path = HISTORY_LOG_PATH) -> None:
    document = {"history": history.get("history", [])}
    path.write_text(json.dumps(document, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")


def _recent_slugs(history: dict[str, list[dict[str, object]]], limit: int) -> set[str]:
    recent: set[str] = set()
    entries = history.get("history", [])
    if not isinstance(entries, list):
        return recent

    for entry in entries[-limit:]:
        slugs = entry.get("slugs") if isinstance(entry, dict) else None
        if isinstance(slugs, list):
            for slug in slugs:
                if isinstance(slug, str):
                    recent.add(slug)
    return recent


def _append_history_entry(history: dict[str, list[dict[str, object]]], date_value: str, slugs: list[str]) -> None:
    entries = history.setdefault("history", [])
    if not isinstance(entries, list):
        entries = history["history"] = []

    if entries and isinstance(entries[-1], dict) and entries[-1].get("date") == date_value:
        entries[-1] = {"date": date_value, "slugs": slugs}
    else:
        entries.append({"date": date_value, "slugs": slugs})

    overflow = len(entries) - HISTORY_MAX_ENTRIES
    if overflow > 0:
        del entries[:overflow]


def select_articles(now: datetime, history: dict[str, list[dict[str, object]]]) -> list[dict[str, object]]:
    selections: list[dict[str, object]] = []
    ordinal = now.date().toordinal()
    recent_slugs = _recent_slugs(history, HISTORY_RECENT_WINDOW)

    for position, category in enumerate(CATEGORY_ORDER):
        pool = ARTICLES[category]
        start_index = (ordinal + position) % len(pool)
        selection: dict[str, object] | None = None
        for offset in range(len(pool)):
            candidate = pool[(start_index + offset) % len(pool)]
            if candidate["slug"] not in recent_slugs:
                selection = candidate
                break
        if selection is None:
            selection = pool[start_index]

        selections.append(selection)
        recent_slugs.add(selection["slug"])

    return selections

def build_html(date_long: str, date_short: str, articles: list[dict[str, object]]) -> str:
    sections = []
    footnotes = []
    for idx, article in enumerate(articles, start=1):
        section_lines = [
            f'<section class="artikel" aria-labelledby="{article["slug"]}">',
            f'<h2 id="{article["slug"]}">{article["title"]}</h2>',
        ]
        for paragraph_index, paragraph in enumerate(article["paragraphs"]):
            if paragraph_index == 0:
                section_lines.append(
                    f'<p>{paragraph}<sup><a id="ref-{idx}" href="#fn-{idx}">[{idx}]</a></sup></p>'
                )
            else:
                section_lines.append(f"<p>{paragraph}</p>")
        section_lines.append("</section>")
        sections.append("\n".join(section_lines))
        footnotes.append(
            f'<li id="fn-{idx}">{article["source_label"]}: "{article["source_title"]}". '
            f'<a href="{article["source_url"]}">{article["source_url"]}</a> '
            f'<a href="#ref-{idx}">Zurueck</a></li>'
        )

    sections_html = "\n".join(sections)
    footnotes_html = "\n".join(footnotes)

    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>history &ndash; {date_long}</title>
<style>
    body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 2rem auto; max-width: 900px; padding: 0 1rem; }}
    header, footer {{ border-bottom: 1px solid #ccc; padding-bottom: 1rem; margin-bottom: 1.5rem; }}
    footer {{ border-top: 1px solid #ccc; border-bottom: none; margin-top: 2rem; padding-top: 1.5rem; }}
    h1, h2, h3 {{ color: #1a1a1a; }}
    section {{ margin-bottom: 2rem; }}
    .meta {{ color: #555; font-size: 0.95rem; }}
    .artikel {{ border-left: 4px solid #1a1a1a; padding-left: 1rem; background: #fafafa; }}
    .artikel p {{ margin: 0.4rem 0; }}
    .footnotes {{ font-size: 0.9rem; }}
    .footnotes li {{ margin-bottom: 0.5rem; }}
</style>
</head>
<body>
<header>
<h1>history</h1>
<p class="meta">update: {date_short}</p>
</header>
<main>
{sections_html}
</main>
<footer>
<section class="footnotes" aria-label="Quellen">
<h3>Quellen</h3>
<ol>
{footnotes_html}
</ol>
</section>
</footer>
</body>
</html>
"""


def build_pdf_content(date_long: str, date_short: str, articles: list[dict[str, object]]) -> bytes:
    lines = [
        "BT",
        "/F1 12 Tf",
        "72 760 Td",
        "(Dokumentation history) Tj",
        "0 -18 Td",
        f"(update: {date_short}) Tj",
        "0 -30 Td",
        "(Automatisierung:) Tj",
        "0 -18 Td",
        "(1. Artikelpool wird taeglich anhand des Datums neu gewaehlt.) Tj",
        "0 -18 Td",
        "(2. Skript ersetzt index.html, tageschronik.html und das PDF vollstaendig.) Tj",
        "0 -18 Td",
        f"(3. GitHub Action aktualisiert Inhalte um {UPDATE_TIME} Uhr.) Tj",
        "0 -18 Td",
        "(4. Quellen werden automatisch als Fussnoten eingefuegt.) Tj",
        "0 -18 Td",
        "(Auswahl des Tages:) Tj",
    ]

    for article in articles:
        title = article["title"]
        if isinstance(title, str):
            if len(title) > 90:
                title = title[:87] + "..."
            title = title.replace("(", "\\(").replace(")", "\\)")
            lines.extend(["0 -18 Td", f"({title}) Tj"])

    lines.extend(
        [
            "0 -30 Td",
            "(Status:) Tj",
            "0 -18 Td",
            "(Dieses PDF dokumentiert den Stand der HTML-Dateien am) Tj",
            "0 -18 Td",
            f"({date_long}) Tj",
            "ET",
        ]
    )
    stream = ("\n".join(lines) + "\n").encode("ascii")
    objs = []
    objs.append(b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n")
    objs.append(b"2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n")
    objs.append(
        b"3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>\nendobj\n"
    )
    objs.append(b"4 0 obj\n<< /Length %d >>\nstream\n" % len(stream) + stream + b"endstream\nendobj\n")
    objs.append(b"5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n")

    parts = [b"%PDF-1.4\n"]
    offsets = [0]
    length = len(parts[0])
    for obj in objs:
        offsets.append(length)
        parts.append(obj)
        length += len(obj)

    xref_pos = length
    xref = [b"xref\n", b"0 6\n", b"0000000000 65535 f \n"]
    for offset in offsets[1:]:
        xref.append(f"{offset:010d} 00000 n \n".encode("ascii"))
    parts.append(b"".join(xref))
    trailer = b"trailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n" + str(xref_pos).encode("ascii") + b"\n%%EOF\n"
    parts.append(trailer)
    return b"".join(parts)


def main() -> None:
    now = datetime.now(ZoneInfo("Europe/Berlin"))
    date_long = german_long_date(now)
    date_short = german_short_date(now)
    history = load_history()
    articles = select_articles(now, history)
    _append_history_entry(history, now.date().isoformat(), [article["slug"] for article in articles])
    save_history(history)

    html_content = build_html(date_long, date_short, articles)
    base_path = BASE_PATH

    for filename in ("index.html", "tageschronik.html"):
        (base_path / filename).write_text(html_content, encoding="utf-8")

    pdf_bytes = build_pdf_content(date_long, date_short, articles)
    (base_path / "dokumentation.pdf").write_bytes(pdf_bytes)


if __name__ == "__main__":
    main()
