from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

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


def german_long_date(dt: datetime) -> str:
    return f"{dt.day}. {MONTHS[dt.month]} {dt.year}"


def german_short_date(dt: datetime) -> str:
    return f"{dt.day}.{dt.month:02d}.{str(dt.year)[-2:]}"


def build_html(date_long: str, date_short: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>neuere geschichte &ndash; {date_long}</title>
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
<h1>neuere geschichte</h1>
<p class="meta">update: {date_short}</p>
</header>
<main>
<section class="artikel" aria-labelledby="politik-1990">
<h2 id="politik-1990">Politik: Deutsche Wiedervereinigung 1990</h2>
<p><strong>Ereignis:</strong> Am 3. Oktober 1990 trat die Deutsche Demokratische Republik auf Grundlage des Einigungsvertrags der Bundesrepublik Deutschland bei, womit die friedliche Revolution von 1989 politisch vollendet und die deutsche Teilung nach vier Jahrzehnten beendet wurde.<sup><a id="ref-1" href="#fn-1">[1]</a></sup> Vorausgegangen waren die Montagsdemonstrationen, die &Ouml;ffnung der innerdeutschen Grenze am 9. November 1989 sowie intensive Zwei-plus-Vier-Verhandlungen mit den Siegerm&auml;chten des Zweiten Weltkriegs, die den &auml;u&szlig;eren Rahmen f&uuml;r die Einheit schufen.</p>
<p><strong>Folgen:</strong> Die institutionelle und wirtschaftliche Zusammenf&uuml;hrung zweier zuvor strikt getrennter Staatssysteme f&uuml;hrte zu Verfassungs- und Verwaltungsreformen, milliardenschweren Aufbauprogrammen sowie einer beschleunigten Integration Deutschlands in die Strukturen der Europ&auml;ischen Gemeinschaft und der NATO. Zugleich entstand eine langanhaltende Transformationsphase mit dem Abbau nicht wettbewerbsf&auml;higer Industrien, massiver Binnenmigration und der Notwendigkeit, unterschiedliche Erinnerungskulturen miteinander zu verbinden.</p>
<p><strong>Was wir gelernt haben:</strong> Dauerhafte Stabilit&auml;t nach Regimewechseln setzt voraus, dass politische Teilhabe erweitert, soziale Disparit&auml;ten aktiv ausgeglichen und au&szlig;enpolitische Partnerschaften gepflegt werden, um Vertrauen in neue demokratische Institutionen zu verankern. Au&szlig;erdem zeigt die Wiedervereinigung, dass neben formalen Vertr&auml;gen auch kulturelle Verst&auml;ndigung, Medienpluralismus und Bildungsangebote entscheidend sind, um geteilte Gesellschaften wieder zusammenzuf&uuml;hren.</p>
<p><strong>Vertiefung:</strong> Die Auseinandersetzung mit den unterschiedlichen Diktaturerfahrungen in Ost- und Westdeutschland pr&auml;gte neue Gedenk- und Bildungsst&auml;tten, w&auml;hrend der Solidarpakt und der L&auml;nderfinanzausgleich bis heute als finanzpolitische Werkzeuge einer Angleichung dienen.</p>
</section>
<section class="artikel" aria-labelledby="wirtschaft-2008">
<h2 id="wirtschaft-2008">Wirtschaft: Globale Finanzkrise 2008</h2>
<p><strong>Ereignis:</strong> Der Kollaps des US-Immobilienmarktes, der Zerfall komplexer Wertpapierketten und die Insolvenz der Investmentbank Lehman Brothers im September 2008 l&ouml;sten eine weltweite Vertrauens- und Liquidit&auml;tskrise im Finanzsystem aus.<sup><a id="ref-2" href="#fn-2">[2]</a></sup> In kurzer Zeit verbreiteten sich Schockwellen &uuml;ber sogenannte Schattenbanken, Kreditversicherungen und Derivatem&auml;rkte in nahezu alle Volkswirtschaften, weil viele Institute identische, schwer bewertbare Produkte hielten.</p>
<p><strong>Folgen:</strong> Regierungen und Zentralbanken stabilisierten Banken mit Garantien, Verstaatlichungen und Notkrediten, legten gro&szlig;e Konjunkturpakete auf und versch&auml;rften die Regulierung durch Ma&szlig;nahmen wie Basel III, Stresstests und Verbraucherschutzauflagen, um das globale Finanzsystem funktionsf&auml;hig zu halten. Arbeitslosigkeit und Staatsverschuldung stiegen an, Immobilienm&auml;rkte korrigierten sich drastisch und in Europa m&uuml;ndete die Krise in die Staatsschuldenproblematik einzelner Eurol&auml;nder, was neue Rettungsmechanismen wie den ESM hervorbrachte.</p>
<p><strong>Was wir gelernt haben:</strong> Systemische Risiken entstehen aus Intransparenz, &Uuml;berhebelung und Anreizkonflikten; nur koordinierte Aufsicht, robuste Eigenkapitalanforderungen und eine Kultur verantwortlichen Risikomanagements verhindern, dass Fehlentwicklungen ganze Volkswirtschaften destabilisieren. Die Krise hat zudem verdeutlicht, dass finanzielle Bildung, klare Haftungsregeln und eine makroprudenzielle Politik n&ouml;tig sind, um spekulative Blasen fr&uuml;hzeitig einzud&auml;mmen.</p>
<p><strong>Vertiefung:</strong> Die globale Finanzkrise f&uuml;hrte zu einem breiten gesellschaftlichen Diskurs &uuml;ber soziale Ungleichheit, die Rolle von Zentralbanken und die Verantwortung internationaler Ratingagenturen, was bis heute Reformen in Unternehmensf&uuml;hrung und Nachhaltigkeitsberichterstattung beeinflusst.</p>
</section>
<section class="artikel" aria-labelledby="zeitgeschichte-2011">
<h2 id="zeitgeschichte-2011">Zeitgeschichte: Reaktorkatastrophe von Fukushima 2011</h2>
<p><strong>Ereignis:</strong> Nach einem schweren Erdbeben der St&auml;rke 9,0 und einem daraus resultierenden Tsunami kam es am 11. M&auml;rz 2011 im japanischen Kernkraftwerk Fukushima Daiichi zu Stromausf&auml;llen, Ausf&auml;llen der K&uuml;hlsysteme, mehreren Kernschmelzen und erheblichen radioaktiven Freisetzungen in Luft und Meer.<sup><a id="ref-3" href="#fn-3">[3]</a></sup> Die Naturkatastrophe zerst&ouml;rte Notstromaggregate, &uuml;berflutete Sicherheitsanlagen und brachte Betreiber, Regierung und internationale Helfer in eine hochkomplexe Notfalllage, in der Entscheidungen unter gro&szlig;em Zeitdruck getroffen werden mussten.</p>
<p><strong>Folgen:</strong> Mehr als 150.000 Menschen mussten langfristig evakuiert werden, gro&szlig;e landwirtschaftliche Fl&auml;chen blieben kontaminiert, Japan initiierte einen umfassenden Energieumbau mit verst&auml;rkten Investitionen in erneuerbare Quellen, und weltweit wurden Sicherheitsstandards, Stresstests sowie Ausstiegsentscheidungen f&uuml;r Kernkraftwerke neu bewertet. Die soziale und psychologische Belastung f&uuml;r die betroffene Bev&ouml;lkerung h&auml;lt bis heute an, und umfangreiche Dekontaminations- sowie R&uuml;ckbauarbeiten werden noch Jahrzehnte beanspruchen.</p>
<p><strong>Was wir gelernt haben:</strong> Der Umgang mit Hochrisikotechnologien verlangt redundante Schutzsysteme, eine Kultur der Sicherheitsvorsorge und eine offene Krisenkommunikation, damit Bev&ouml;lkerung, Politik und Betreiber fr&uuml;hzeitig auf Worst-Case-Szenarien vorbereitet sind. Fukushima hat zudem deutlich gemacht, dass Klimawandel-bedingte Extremereignisse in Risikobewertungen st&auml;rker ber&uuml;cksichtigt und internationale Notfallkooperationen ge&uuml;bt werden m&uuml;ssen.</p>
<p><strong>Vertiefung:</strong> Die Katastrophe beschleunigte in Deutschland den beschlossenen Ausstieg aus der Kernenergie, verst&auml;rkte weltweit die Forschung an Speichertechnologien und f&uuml;hrte zur Einrichtung neuer unabh&auml;ngiger Sicherheitsbeh&ouml;rden mit erweiterten Pr&uuml;fkompetenzen.</p>
</section>
<section class="artikel" aria-labelledby="fruehneuzeit-1789">
<h2 id="fruehneuzeit-1789">Gesellschaft: Franz&ouml;sische Revolution 1789</h2>
<p><strong>Ereignis:</strong> Am 14. Juli 1789 st&uuml;rmte die Pariser Bev&ouml;lkerung die Bastille und setzte damit den Auftakt f&uuml;r einen tiefgreifenden politischen und gesellschaftlichen Wandel in Frankreich, der zur Abschaffung der Feudalordnung, zur Erkl&auml;rung der Menschen- und B&uuml;rgerrechte und zur Umgestaltung staatlicher Macht f&uuml;hrte.<sup><a id="ref-4" href="#fn-4">[4]</a></sup> In den folgenden Jahren pr&auml;gten verfassunggebende Versammlungen, der politisierte Adel, radikale Clubs und milit&auml;rische Auseinandersetzungen das Kr&auml;ftefeld Europas.</p>
<p><strong>Folgen:</strong> Die Revolution inspirierte Bewegungen in ganz Europa und Amerika, verbreitete egalit&auml;re Ideale, f&uuml;hrte aber auch zu Gewaltphasen wie der Schreckensherrschaft sowie zu Gegenreaktionen monarchischer M&auml;chte. Langfristig l&ouml;ste sie tiefgreifende Reformen in Verwaltung, Rechtsordnung und Bildung aus und bildete den N&auml;hrboden f&uuml;r moderne Nationalstaatskonzepte.</p>
<p><strong>Was wir gelernt haben:</strong> Gesellschaftlicher Wandel ben&ouml;tigt legitime Partizipationskan&auml;le und stabile Institutionen; ohne sie drohen revolution&auml;re Dynamiken in Gewalt und Autoritarismus umzuschlagen. Die Revolution verdeutlicht, wie wichtig eine breite Repr&auml;sentation und soziale Absicherung f&uuml;r die Akzeptanz politischer Systeme ist.</p>
<p><strong>Vertiefung:</strong> Die Debatten um Freiheit, Gleichheit und Br&uuml;derlichkeit beeinflussten das V&ouml;lkerrecht, die Entwicklung parlamentarischer Systeme und die Codifizierung universeller Menschenrechte, deren Wirkung bis in moderne Verfassungen reicht.</p>
</section>
<section class="artikel" aria-labelledby="antike-0027">
<h2 id="antike-0027">Antike: Beginn der Pax Romana 27 v. Chr.</h2>
<p><strong>Ereignis:</strong> Mit der Macht&uuml;bernahme Octavians als Augustus im Jahr 27 v. Chr. konsolidierte sich das R&ouml;mische Reich nach langj&auml;hrigen B&uuml;rgerkriegen und trat in eine jahrzehntelange Phase relativen Friedens, wirtschaftlicher Stabilit&auml;t und territorialer Expansion ein, die als Pax Romana bekannt wurde.<sup><a id="ref-5" href="#fn-5">[5]</a></sup> Reorganisationen von Heer, Verwaltung und Infrastruktur legten die Grundlage f&uuml;r eine zentral gesteuerte Reichsordnung.</p>
<p><strong>Folgen:</strong> Die Pax Romana f&ouml;rderte Handel, St&auml;dtebau und kulturellen Austausch im gesamten Mittelmeerraum, stabilisierte Grenzregionen und erm&ouml;glichte den Ausbau von Rechtssystemen sowie Verkehrswegen wie Stra&szlig;en und Aqu&auml;dukten. Gleichzeitig sicherte sie die Macht des Princeps und ver&auml;nderte die politische Kultur Roms dauerhaft zugunsten eines kaiserlichen Systems.</p>
<p><strong>Was wir gelernt haben:</strong> Nachhaltige Friedensordnungen entstehen durch legitime Machtstrukturen, effiziente Verwaltung und wirtschaftliche Integration; sie bleiben jedoch anf&auml;llig, wenn politische Nachfolge ungekl&auml;rt und regionale Interessen unber&uuml;cksichtigt bleiben. Die Pax Romana illustriert, wie Infrastruktur und Rechtssicherheit zur Stabilisierung gro&szlig;er politischer Einheiten beitragen.</p>
<p><strong>Vertiefung:</strong> Der kulturelle Austausch w&auml;hrend der Pax Romana verbreitete lateinische Sprache, r&ouml;misches Recht und technische Innovationen, was die Grundlage f&uuml;r europ&auml;ische Rechts- und Verwaltungstraditionen sowie f&uuml;r das Netzwerk von Handelsrouten legte, auf denen sp&auml;tere Religionen und Ideen reisten.</p>
</section>
</main>
<footer>
<section class="footnotes" aria-label="Quellen">
<h3>Quellen</h3>
<ol>
<li id="fn-1">Bundeszentrale f&uuml;r politische Bildung: "Der Weg zur Deutschen Einheit". <a href="https://www.bpb.de/themen/deutsche-einheit/">https://www.bpb.de/themen/deutsche-einheit/</a> <a href="#ref-1">Zur&uuml;ck</a></li>
<li id="fn-2">International Monetary Fund: "The Great Recession" (World Economic Outlook 2009). <a href="https://www.imf.org/en/Publications/WEO/Issues/2016/12/31/World-Economic-Outlook-October-2009-Sustaining-the-Recovery-23332">https://www.imf.org/en/Publications/WEO/Issues/2016/12/31/World-Economic-Outlook-October-2009-Sustaining-the-Recovery-23332</a> <a href="#ref-2">Zur&uuml;ck</a></li>
<li id="fn-3">International Atomic Energy Agency: "Fukushima Daiichi Accident Report". <a href="https://www.iaea.org/publications/10962/the-fukushima-daiichi-accident">https://www.iaea.org/publications/10962/the-fukushima-daiichi-accident</a> <a href="#ref-3">Zur&uuml;ck</a></li>
<li id="fn-4">Encyclopaedia Britannica: "French Revolution". <a href="https://www.britannica.com/event/French-Revolution">https://www.britannica.com/event/French-Revolution</a> <a href="#ref-4">Zur&uuml;ck</a></li>
<li id="fn-5">Encyclopaedia Britannica: "Pax Romana". <a href="https://www.britannica.com/event/Pax-Romana">https://www.britannica.com/event/Pax-Romana</a> <a href="#ref-5">Zur&uuml;ck</a></li>
</ol>
</section>
</footer>
</body>
</html>
"""


def build_pdf_content(date_long: str, date_short: str) -> bytes:
    lines = [
        "BT",
        "/F1 12 Tf",
        "72 760 Td",
        "(Dokumentation neuere geschichte) Tj",
        "0 -18 Td",
    f"(update: {date_short}) Tj",
        "0 -30 Td",
        "(Automatisierung:) Tj",
        "0 -18 Td",
        "(1. index.html dient als Einstieg fuer GitHub Pages und stimmt) Tj",
        "0 -18 Td",
        "(   inhaltlich mit tageschronik.html ueberein.) Tj",
        "0 -18 Td",
        "(2. Beide HTML-Dateien enthalten fuenf Ressorts zu Politik,) Tj",
        "0 -18 Td",
        "(   Wirtschaft, Zeitgeschichte, Gesellschaft und Antike.) Tj",
    "0 -18 Td",
    f"(3. GitHub Action aktualisiert Inhalte taeglich um {UPDATE_TIME} Uhr.) Tj",
        "0 -18 Td",
        f"(4. Titel aktualisiert auf {date_long}.) Tj",
        "0 -18 Td",
        "(5. Quellen werden weiterhin als Fussnoten gepflegt.) Tj",
        "0 -30 Td",
        "(Status:) Tj",
        "0 -18 Td",
        "(Dieses PDF dokumentiert den Stand der HTML-Dateien am) Tj",
        "0 -18 Td",
        f"({date_long}.) Tj",
        "ET",
    ]
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

    html_content = build_html(date_long, date_short)
    base_path = Path(__file__).resolve().parent

    for filename in ("index.html", "tageschronik.html"):
        (base_path / filename).write_text(html_content, encoding="utf-8")

    pdf_bytes = build_pdf_content(date_long, date_short)
    (base_path / "dokumentation.pdf").write_bytes(pdf_bytes)


if __name__ == "__main__":
    main()
