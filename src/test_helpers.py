import pytest
from helpers import text_node_to_html_node
from textnode import TextNode, TextType


def test_text():
    node = TextNode("This is a text node", TextType.PLAIN)
    html_node = text_node_to_html_node(node)
    assert html_node.tag is None
    assert html_node.value == "This is a text node"


def test_bold():
    node = TextNode("This is a text node", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    assert html_node.tag is "b"
    assert html_node.value == "This is a text node"


def test_italic():
    node = TextNode("This is a text node", TextType.ITALIC)
    html_node = text_node_to_html_node(node)
    assert html_node.tag is "i"
    assert html_node.value == "This is a text node"


def test_code():
    node = TextNode("This is a text node", TextType.CODE)
    html_node = text_node_to_html_node(node)
    assert html_node.tag is "code"
    assert html_node.value == "This is a text node"


@pytest.mark.parametrize(
    "tag, want",
    [
        (TextType.PLAIN, "This is a text node"),
        (TextType.BOLD, "<b>This is a text node</b>"),
        (TextType.ITALIC, "<i>This is a text node</i>"),
        (TextType.CODE, "<code>This is a text node</code>"),
        (TextType.LINK, '<a href="example.com">This is a text node</a>'),
        (TextType.IMAGE, '<img src="example.com" alt="This is a text node"></img>'),
    ],
)
def test_text_node_to_html_node(tag, want):
    url = "example.com" if tag in [TextType.LINK, TextType.IMAGE] else None
    node = TextNode("This is a text node", tag, url)
    html_node = text_node_to_html_node(node).to_html()
    assert str(html_node) == want
