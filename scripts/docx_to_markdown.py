from __future__ import annotations

import re
import sys
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def para_text(p: ET.Element) -> str:
    parts: list[str] = []
    for node in p.iter():
        if node.tag == W + "t":
            parts.append(node.text or "")
        elif node.tag == W + "tab":
            parts.append("\t")
        elif node.tag == W + "br":
            parts.append("\n")
    return "".join(parts).strip()


def markdown_block(text: str, index: int) -> str:
    if index == 0:
        return f"# {text}"

    if "\n" in text:
        first, rest = text.split("\n", 1)
        if first.isupper():
            return f"## {first.strip()}\n\n{rest.strip()}"

    if re.match(r"^(PROLOGUE|CHAPTER|EPILOGUE)\b", text, re.IGNORECASE):
        return f"## {text}"

    if text.isupper() and len(text) <= 90:
        return f"## {text}"

    return text


def convert_docx_to_markdown(src: Path, dest: Path) -> None:
    with ZipFile(src) as zf:
        root = ET.fromstring(zf.read("word/document.xml"))

    blocks: list[str] = []
    for p in root.iter(W + "p"):
        text = para_text(p)
        if text:
            blocks.append(markdown_block(text, len(blocks)))

    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text("\n\n".join(blocks) + "\n", encoding="utf-8")


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python3 scripts/docx_to_markdown.py <source.docx> <dest.md>")
    convert_docx_to_markdown(Path(sys.argv[1]), Path(sys.argv[2]))


if __name__ == "__main__":
    main()
