from generate_page import generate_page
from textnode import TextNode, TextType
from copy_static import copy_static, empty_dir
from pathlib import Path


def main():
    public = Path("public")
    static = Path("static")
    empty_dir(public)
    copy_static(static, public)
    content = Path("content")
    template = Path("template.html")
    generate_page(content / "index.md", public / "index.html", template)
    print("Done")


if __name__ == "__main__":
    main()
