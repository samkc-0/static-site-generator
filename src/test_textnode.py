import pytest
from typing import Text
from textnode import TextNode, TextType


def test_textnode_equality():
    a = TextNode("Hello", TextType.PLAIN)
    b = TextNode("Hello", TextType.PLAIN)
    assert a == b


def test_textnode_text_inequality():
    a = TextNode("Hello", TextType.PLAIN)
    b = TextNode("Goodbye", TextType.PLAIN)
    assert a != b


def test_textnode_texttype_inequality():
    a = TextNode("Hello", TextType.PLAIN)
    b = TextNode("Hello", TextType.BOLD)
    assert a != b


def test_textnode_url_inequality():
    a = TextNode("Hello", TextType.LINK, "https://www.google.com")
    b = TextNode("Hello", TextType.LINK, "https://crt.sh")
    assert a != b


def test_textnode_repr_with_url():
    # <a>
    link = TextNode("google", TextType.LINK, "https://www.google.com")
    assert (
        repr(link)
        == "TextNode(text='google', text_type=TextType.LINK, url='https://www.google.com')"
    )
    # <img src=...>
    src = "https://placecats.com/g/300/200"
    img = TextNode("a cat", TextType.IMAGE, src)
    assert (
        repr(img)
        == "TextNode(text='a cat', text_type=TextType.IMAGE, url='https://placecats.com/g/300/200')"
    )


def test_textnode_repr_for_non_links():
    t = TextNode("Hello", TextType.PLAIN)
    assert repr(t) == "TextNode(text='Hello', text_type=TextType.PLAIN)"


def test_only_images_and_links_can_have_urls():
    with pytest.raises(ValueError):
        TextNode(
            "This is just some bold text.", TextType.BOLD, "https://www.google.com"
        )
