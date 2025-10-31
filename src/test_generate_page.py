import pytest
from typing import Generator
from pathlib import Path
from tempfile import TemporaryDirectory, TemporaryFile
from generate_page import extract_title, generate_pages


def test_extract_title():
    assert extract_title("# This is a title") == "This is a title"
    assert (
        extract_title("this is not the title\n# but this is\n## and this is not")
        == "but this is"
    )


test_md = """# Contact the Author

[< Back Home](/)

Give me a call anytime to chat!

`555-555-5555`

**"Váya márië."**"""


template_html = """
    <!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{{ Title }}</title>
    <link href="/index.css" rel="stylesheet" />
  </head>

  <body>
    <article>{{ Content }}</article>
  </body>
</html>"""


@pytest.fixture(scope="module", name="template")
def template():
    with TemporaryDirectory() as tmp:
        template = Path(tmp) / "template.html"
        template.write_text(template_html)
        yield template


@pytest.fixture(scope="module", name="content")
def content():
    with TemporaryDirectory() as tmp:
        content = Path(tmp) / "content"
        content.mkdir(exist_ok=True)
        index_md = content / "index.md"
        index_md.write_text(test_md)
        blog = content / "blog"
        blog.mkdir()
        index_md = blog / "index.md"
        index_md.write_text(test_md)
        yield content


@pytest.fixture(scope="module", name="public")
def public():
    with TemporaryDirectory() as tmp:
        public = Path(tmp) / "public"
        public.mkdir(exist_ok=True)
        yield public


def test_generate_page(content, public, template):
    generate_pages(content, public, template)
    assert (public / "index.html").is_file()
    assert (public / "blog" / "index.html").is_file()
    html = (public / "index.html").read_text()
    assert "<title>Contact the Author</title>" in html
    assert "<h1>Contact the Author</h1>" in html
    html = (public / "blog" / "index.html").read_text()
    assert "<title>Contact the Author</title>" in html
    assert "<h1>Contact the Author</h1>" in html
