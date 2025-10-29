from parser import (
    tokenize,
    code_pattern,
    link_pattern,
    image_pattern,
)
from textnode import TextNode, TextType


def test_tokenize_code_block():
    tokens = list(tokenize("This is text with a `code block` word", [code_pattern]))
    assert tokens == [
        ("This is text with a ", None),
        ("code block", "code"),
        (" word", None),
    ]


def test_tokenize_link():
    tokens = list(
        tokenize("This is text with an [example](www.example.com) link", [link_pattern])
    )
    assert tokens == [
        ("This is text with an ", None),
        ("[example](www.example.com)", "link"),
        (" link", None),
    ]


def test_tokenize_image_takes_precedence_over_link():
    tokens = list(
        tokenize(
            "This is text with an ![alt text](image.png) image",
            [image_pattern, link_pattern],
        )
    )
    assert tokens == [
        ("This is text with an ", None),
        ("![alt text](image.png)", "image"),
        (" image", None),
    ]
