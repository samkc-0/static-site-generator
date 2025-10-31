from generate_page import generate_pages
from textnode import TextNode, TextType
from copy_static import copy_static, empty_dir
from pathlib import Path
import sys


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    public = Path("public") if len(sys.argv) <= 2 else Path(sys.argv[2])
    static = Path("static")
    empty_dir(public)
    copy_static(static, public)
    content = Path("content")
    template = Path("template.html")
    generate_pages(content, public, template, basepath)
    print("Done")


if __name__ == "__main__":
    main()
