from functools import wraps
import pytest
from helpers import md_to_html_node


test_cases = [
    ("# This is an H1 heading", "<h1>This is an H1 heading</h1>"),
    ("## This is an H2 heading", "<h2>This is an H2 heading</h2>"),
    ("### This is an H3 heading", "<h3>This is an H3 heading</h3>"),
    ("#### This is an H4 heading", "<h4>This is an H4 heading</h4>"),
    ("##### This is an H5 heading", "<h5>This is an H5 heading</h5>"),
    ("###### This is an H6 heading", "<h6>This is an H6 heading</h6>"),
    ("This is an ordinary paragraph", "<p>This is an ordinary paragraph</p>"),
    ("This p has some **bold** text", "<p>This p has some <b>bold</b> text</p>"),
    (
        "```#include <stdio.h>\n#include <stdlib.h>```",
        "<pre><code>#include <stdio.h>\n#include <stdlib.h></code></pre>",
    ),
    (
        "> This is a blockquote",
        "<blockquote>This is a blockquote</blockquote>",
    ),
    (
        "- this is important\n- and so is this",
        "<ul><li>this is important</li><li>and so is this</li></ul>",
    ),
    (
        "1. first item\n2. second item",
        "<ol><li>first item</li><li>second item</li></ol>",
    ),
]


@pytest.mark.parametrize("markdown, want", test_cases)
def test_md_to_html_node(markdown, want):
    node = md_to_html_node(markdown)
    assert node.to_html() == f"<div>{want}</div>"


def test_paragraphs():
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

    node = md_to_html_node(md)
    html = node.to_html()
    assert (
        html
        == """<div><p>This is <b>bolded</b> paragraph
text in a p
tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"""
    )


def test_codeblock():
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = md_to_html_node(md)
    html = node.to_html()
    assert (
        html
        == """<div><pre><code>
This is text that _should_ remain
the **same** even with inline stuff
</code></pre></div>"""
    )
