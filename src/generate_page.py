from pathlib import Path
from helpers import md_to_html_node


def extract_title(page: str):
    for line in page.split("\n"):
        if line.startswith("# "):
            return line[2:]
    return "untitled"


def generate_page(src: Path, dst: Path, template: Path, basepath: str = "/"):
    print(f"Generating page  from {src} to {dst} using {template}")
    md = src.read_text()
    title = extract_title(md)
    content = md_to_html_node(md).to_html()
    as_html = (
        template.read_text()
        .replace("{{ Title }}", title)
        .replace("{{ Content }}", content)
        .replace('href="/', f'href="{basepath}')
        .replace('src="/', f'src="{basepath}')
    )
    dst.parent.mkdir(exist_ok=True)
    dst.write_text(as_html)


def generate_pages(src: Path, dst: Path, template: Path, basepath: str = "/"):
    for p in src.iterdir():
        if p.is_file() and p.name == "index.md":
            generate_page(p, dst / f"{p.stem}.html", template, basepath)
        if p.is_dir():
            copied = dst / p.name
            copied.mkdir(exist_ok=True)
            generate_pages(p, copied, template, basepath)
