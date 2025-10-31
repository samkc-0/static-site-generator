from pathlib import Path
from helpers import md_to_html_node


def extract_title(page: str):
    for line in page.split("\n"):
        if line.startswith("# "):
            return line[2:]
    return "untitled"


def generate_page(src: Path, dst: Path, template: Path):
    print(f"Generating page  from {src} to {dst} using {template}")
    md = src.read_text()
    title = extract_title(md)
    content = md_to_html_node(md).to_html()
    as_html = (
        template.read_text()
        .replace("{{ Title }}", title)
        .replace("{{ Content }}", content)
    )
    dst.parent.mkdir(exist_ok=True)
    dst.write_text(as_html)
