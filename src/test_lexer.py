import pytest
from lexer import lex
from textnode import TextNode, TextType


@pytest.mark.parametrize(
    "tokens, want",
    [
        (
            ["This is text with a ", "`", "code block", "`", "word"],
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("code block", TextType.CODE),
                TextNode("word", TextType.PLAIN),
            ],
        ),
        (
            ["This is text with a ", "**", "bold block", "**", "word"],
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("bold block", TextType.BOLD),
                TextNode("word", TextType.PLAIN),
            ],
        ),
        (
            ["This is text with a ", "*", "italic block", "*", "word"],
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("italic block", TextType.ITALIC),
                TextNode("word", TextType.PLAIN),
            ],
        ),
        (
            [
                "This sentence contains ",
                "**",
                "bold text",
                "**" " and ",
                "_",
                "italic text",
                "_",
                " and ",
                "`",
                "even some code",
                "`",
                ".",
            ],
            [
                TextNode("This sentence contains ", TextType.PLAIN),
                TextNode("bold text", TextType.BOLD),
                TextNode(" and ", TextType.PLAIN),
                TextNode("italic text", TextType.ITALIC),
                TextNode(" and ", TextType.PLAIN),
                TextNode("even some code", TextType.CODE),
                TextNode(".", TextType.PLAIN),
            ],
        ),
    ],
)
def test_lexer(tokens, want):
    tokens = ["This is text with a ", "`", "code block", "`", "word"]
    got = lex(tokens)
    want = [
        TextNode("This is text with a ", TextType.PLAIN),
        TextNode("code block", TextType.CODE),
        TextNode("word", TextType.PLAIN),
    ]
    assert got == want, f"got {got}, want {want}"
