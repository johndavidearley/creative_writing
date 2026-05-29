from __future__ import annotations

import copy
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from xml.etree import ElementTree as ET

SRC = Path("/mnt/c/Users/johnd/Downloads/EOTLL.docx")
OUT_DOCX = Path("/tmp/EOTLL.report-revision.docx")
OUT_MD = Path("manuscripts/EOTLL.report-revision.md")

NS_W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
W = f"{{{NS_W}}}"

ET.register_namespace("w", NS_W)
ET.register_namespace("r", "http://schemas.openxmlformats.org/officeDocument/2006/relationships")
ET.register_namespace("wp", "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing")
ET.register_namespace("a", "http://schemas.openxmlformats.org/drawingml/2006/main")
ET.register_namespace("pic", "http://schemas.openxmlformats.org/drawingml/2006/picture")
ET.register_namespace("w14", "http://schemas.microsoft.com/office/word/2010/wordml")
ET.register_namespace("w15", "http://schemas.microsoft.com/office/word/2012/wordml")
ET.register_namespace("mc", "http://schemas.openxmlformats.org/markup-compatibility/2006")


def para_text(p: ET.Element) -> str:
    return "".join(t.text or "" for t in p.iter(W + "t")).strip()


def set_para_text(p: ET.Element, text: str) -> None:
    ppr = p.find(W + "pPr")
    for child in list(p):
        p.remove(child)
    if ppr is not None:
        p.append(ppr)

    run = ET.SubElement(p, W + "r")
    t = ET.SubElement(run, W + "t")
    if text[:1].isspace() or text[-1:].isspace():
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    t.text = text


def make_para(template: ET.Element, text: str) -> ET.Element:
    p = copy.deepcopy(template)
    set_para_text(p, text)
    return p


def nonempty_paras(root: ET.Element) -> list[ET.Element]:
    return [p for p in root.iter(W + "p") if para_text(p)]


def insert_after(body: ET.Element, existing: ET.Element, new_paras: list[ET.Element]) -> None:
    children = list(body)
    idx = children.index(existing)
    for offset, p in enumerate(new_paras, 1):
        body.insert(idx + offset, p)


def replace_span(body: ET.Element, start: ET.Element, end: ET.Element, new_paras: list[ET.Element]) -> None:
    children = list(body)
    start_idx = children.index(start)
    end_idx = children.index(end)
    for child in children[start_idx : end_idx + 1]:
        body.remove(child)
    for offset, p in enumerate(new_paras):
        body.insert(start_idx + offset, p)


PROLOGUE_INSERT = [
    "Markov did not look first at the dead waveform.",
    "He looked at the locked column of the launch roster, where one name had already turned from contingency amber to mission red: RAINES, EIRA. The council had not voted. DEFCON Eclipse was still a sealed protocol buried under layers of authorization and denial. But the signal had already made the decision feel less like strategy than arithmetic.",
    "In less than an hour, if he could make his hand obey him, he would order one commander to leave everyone she had ever known behind and carry the species as cargo. Not to win. Not even to fight. To ensure that losing would not be the last human act.",
]

CHAPTER_1_REPLACEMENT = [
    "Twelve minutes. Twelve minutes was all it took for the ghost signal from Proxima Centauri to ripple outward and turn the Planetary Defense Council from a governing body into a jury deciding how much of humanity could be abandoned in order to preserve the rest.",
    "Beneath Lunar Command's Tranquility surface dome, the briefing theater felt less like a seat of power than a sealed chamber waiting for sentence to be passed. Tablets glowed on polished desks. A curved map of the Sol-Proxima corridor rotated across the wall, its far end no longer a bright artery of expansion but a ragged red wound blinking where a colony had been.",
    "Admiral Konstantin Markov stepped onto the podium without notes. He did not need them. The transmission had burned itself into him.",
    "\"Playback,\" he said.",
    "The voices returned through the acoustic emitters: gasps torn into static, overlapping pleas, fragments of language breaking apart around that low, living subharmonic. When the last word faded--erase--the room remained silent long enough for the ventilation to sound accusatory.",
    "Dr. Hana Saito activated her console. Spectrographic charts and biometric extrapolations rose above her desk in cold blue layers. \"What we heard was not a distress call,\" she said. \"It was an autopsy conducted by the victims while the body was still failing.\"",
    "General Bach, head of Unified Space Command, tapped two fingers against the waveform display. \"Call it what it is. A weapon.\"",
    "Saito did not look away from the red static. \"That would be convenient.\"",
    "\"Convenient?\"",
    "\"A weapon has a wielder. A motive. A supply line. Something your fleets can make dead.\" She turned at last. \"This does not hate us, General. I am not sure it notices us.\"",
    "The council absorbed that in a silence more complete than agreement.",
    "\"If it does not notice us,\" said Councilor Reyes, one of the corporate ministers, \"why is the secondary trail pointed at Sol?\"",
    "On the back bench, Analyst Second Class Rodrigo Velasquez raised his hand halfway, as if hoping someone would tell him not to continue. No one did. He stood, young face pale in the map glow, and sent his findings to the central display.",
    "A chain of amber points appeared between Proxima and Sol.",
    "\"Deep Scan V-177 registered secondary energy bursts during the blackout,\" Velasquez said. His voice caught, then steadied as he retreated into data. \"Minimal power, nearly lost in background noise. But the bursts carry the same subharmonic signature as the transmission. They are propagating outward from Proxima. Toward us.\"",
    "Bach leaned forward. \"Speed?\"",
    "\"Variable. Not ballistic. Not light-limited in any model we trust.\"",
    "That did it. The ministers understood timetables. They understood markets, evacuations, liabilities. They did not understand a deadline that refused physics.",
    "Markov let them sit with the implication for three breaths. \"Targets?\"",
    "Velasquez swallowed. \"Not population centers. Not orbital docks. Not habitats. The first losses were research facilities: Xenomaterials Analysis, Theoretical Physics, Deep Core Survey. The places studying the artifacts recovered under Proxima's crust.\" He looked up then, unable to hide the thought that had ruined his face. \"It looks as if knowledge itself was the infection.\"",
    "A chair creaked somewhere in the upper tier. No one turned.",
    "Saito's hands went still over her console. \"The Obelisk fragments.\"",
    "Markov folded his hands behind his back. It was an old command posture, useful because it kept men from seeing whether your fingers trembled. \"Artifacts retrieved from the Proxima Deep Core Survey six months ago, under Directive Seven-Gamma, are currently stored in high containment. Quarantine Lab Seven. Lunar orbit.\"",
    "The room changed temperature without the environmental systems moving a degree.",
    "\"Here?\" Saito asked.",
    "\"Lunar orbit,\" Markov repeated.",
    "Bach's chair scraped back. \"You let an extinction vector inside the system?\"",
    "Markov did not defend himself. \"I let a classified research program continue because every model said the fragments were inert.\"",
    "\"And now?\"",
    "\"Now the models are dead with Proxima.\"",
    "The minister with the cufflink chrono shut his display. For the first time since entering the room, he stopped checking the markets.",
    "\"Destroy them,\" Bach said. \"Incinerate the lab. Vaporize the debris.\"",
    "\"No,\" Saito said, too quickly.",
    "Bach rounded on her. \"Doctor, if your objection is scientific preservation--\"",
    "\"My objection is ignorance. We do not know whether destroying the fragments silences the signal or rings the bell louder.\"",
    "Markov keyed a sealed file. The words DEFCON ECLIPSE filled the chamber in white letters.",
    "\"This vote authorizes strategic removal of the Ark core, related artifacts, and selected knowledge archives from Sol control,\" he said. \"It also authorizes denial protocols for anything we cannot move.\"",
    "\"Denial,\" Saito said softly. \"You mean destruction.\"",
    "\"I mean preventing our memory from becoming a beacon.\"",
    "Reyes stared at the protocol text. \"The public will panic if archives go dark.\"",
    "\"The public will panic if the sky starts subtracting cities,\" Bach said.",
    "Markov let the exchange burn itself out. He had one more truth, and he knew exactly when to use it. \"The Solace launches within the hour. Ark vault authority transfers to Commander Eira Raines once she clears lunar gravity. After that, no ground override remains.\"",
    "Saito looked up sharply. \"One pilot?\"",
    "\"One pilot and Helios.\"",
    "\"You are sending her beyond recall,\" Reyes said.",
    "\"I am sending her beyond capture.\"",
    "For a moment, no one spoke. The difference between those sentences settled across the chamber like dust.",
    "The vote required biometric confirmation from every member. One by one, lights blinked green. The military chiefs moved first. The scientists followed, not with agreement but with recognition of the narrowing trap. The corporate ministers hesitated long enough to reveal the arithmetic they were still performing, then pressed their palms to the glass.",
    "Unanimous.",
    "But the silence that followed felt anything but united. It carried Proxima's dead voices, the weight of abandoned colonies, the planned destruction of archives, and the name of a commander most of them had never met but had just condemned to become the custodian of a species.",
    "Markov stared at the amber trail pointing home. DEFCON Eclipse was active. The clock was ticking. Somewhere across the lunar plain, Eira Raines was being sealed into a flight suit.",
]

CHAPTER_3_OLD_START = "Eira accepted the rod. It felt cool and heavy"
CHAPTER_3_OLD_END = "Markov took a half-step back"

CHAPTER_3_REPLACEMENT = [
    "Eira accepted the rod. It felt cool and heavy in her gloved palm, dense with unimaginable weight--the sum total of human knowledge, culture, folly, and brilliance. \"No override?\" she confirmed, meeting his gaze directly.",
    "\"None.\"",
    "\"Then this isn't a mission transfer,\" she said. \"It's exile with a launch window.\"",
    "Markov absorbed the blow without flinching. \"It is survival placed beyond negotiation.\"",
    "\"And if I decide survival requires something other than the plan?\"",
    "For the first time since entering, his command mask cracked enough to show the exhausted man beneath it. \"Then make the decision where we cannot stop you. That is the point.\"",
    "The answer frightened her more than an order would have. Orders could be obeyed, resisted, appealed. Trust was a weight with no handles.",
    "\"We either trust you, Commander Raines,\" he said, voice lower now, \"or we are already extinct and this is just arranging the epitaph.\"",
    "He took a half-step back, breaking the intensity of the moment before emotions could fully surface and fossilize into words that might compromise them both. \"Make us remembered,\" he said. The command came out almost as a plea.",
    "Then he was gone, leaving only the faint scent of ozone and the heavy silence behind.",
]


def main() -> None:
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(SRC, "r") as zin:
        document_xml = zin.read("word/document.xml")
        root = ET.fromstring(document_xml)
        body = root.find(W + "body")
        if body is None:
            raise RuntimeError("Could not find document body")

        paras = nonempty_paras(root)

        prologue_anchor = next(p for p in paras if para_text(p).startswith("For a terrifying, suspended heartbeat"))
        normal_template = next(p for p in paras if para_text(p).startswith("Twelve minutes. Twelve minutes"))
        insert_after(body, prologue_anchor, [make_para(normal_template, text) for text in PROLOGUE_INSERT])

        paras = nonempty_paras(root)
        chapter_1_start = next(p for p in paras if para_text(p).startswith("Twelve minutes. Twelve minutes"))
        chapter_1_end = next(p for p in paras if para_text(p).startswith("Markov stared at the map"))
        replace_span(body, chapter_1_start, chapter_1_end, [make_para(chapter_1_start, text) for text in CHAPTER_1_REPLACEMENT])

        paras = nonempty_paras(root)
        ch3_start = next(p for p in paras if para_text(p).startswith(CHAPTER_3_OLD_START))
        ch3_end = next(p for p in paras if para_text(p).startswith(CHAPTER_3_OLD_END))
        replace_span(body, ch3_start, ch3_end, [make_para(ch3_start, text) for text in CHAPTER_3_REPLACEMENT])

        updated_xml = ET.tostring(root, encoding="utf-8", xml_declaration=True)

        with ZipFile(OUT_DOCX, "w", ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                if item.filename == "word/document.xml":
                    data = updated_xml
                zout.writestr(item, data)

    from docx_to_markdown import convert_docx_to_markdown

    convert_docx_to_markdown(OUT_DOCX, OUT_MD)
    print(OUT_MD)


if __name__ == "__main__":
    main()
