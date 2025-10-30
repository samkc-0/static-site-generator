from parser import (
    lex,
    tokenize,
    code_pattern,
    link_pattern,
    image_pattern,
)
from textnode import TextNode, TextType


def test_tokenize_code_block():
    tokens = list(tokenize("This is text with a `code block` word", [code_pattern]))
    assert tokens == [
        ("This is text with a ", "plain"),
        ("code block", "code"),
        (" word", "plain"),
    ]


def test_tokenize_link():
    tokens = list(
        tokenize("This is text with an [example](www.example.com) link", [link_pattern])
    )
    assert tokens == [
        ("This is text with an ", "plain"),
        ("[example](www.example.com)", "link"),
        (" link", "plain"),
    ]


def test_tokenize_image_takes_precedence_over_link():
    tokens = list(
        tokenize(
            "This is text with an ![alt text](image.png) image",
            [image_pattern, link_pattern],
        )
    )
    assert tokens == [
        ("This is text with an ", "plain"),
        ("![alt text](image.png)", "image"),
        (" image", "plain"),
    ]


def test_lexer():
    tokens = list(
        tokenize(
            "This is **bold text** with an [example](www.example.com) link",
        )
    )
    nodes = list(lex(tokens))
    assert nodes == [
        TextNode("This is ", TextType.PLAIN),
        TextNode("bold text", TextType.BOLD),
        TextNode(" with an ", TextType.PLAIN),
        TextNode("example", TextType.LINK, url="www.example.com"),
        TextNode(" link", TextType.PLAIN),
    ]
