from parser import split_nodes_delimiter
from textnode import TextNode, TextType


def test_split_nodes_delmiter():
    node = TextNode("This is text with a `code block` word", TextType.PLAIN)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    assert new_nodes == [
        TextNode("This is text with a ", TextType.PLAIN),
        TextNode("code block", TextType.CODE),
        TextNode(" word", TextType.PLAIN),
    ]
