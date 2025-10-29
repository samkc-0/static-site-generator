from typing import Callable
from functools import partial
from textnode import TextNode, TextType
import re


bold_pattern = r"\*\*(?P<bold>.*?)\*\*"
italic_pattern = r"_(?P<italic>.*?)_"
code_pattern = r"`(?P<code>[^`\n].*?)`"
link_pattern = r"!{0}(?P<link>\[.*?\]\(.*?\))"
image_pattern = r"(?P<image>!\[.*?\]\(.*?\))"

PATTERNS = [bold_pattern, italic_pattern, code_pattern, image_pattern, link_pattern]


def tokenize(text, patterns=PATTERNS):
    pattern = re.compile("|".join(patterns))
    last = 0
    matches = list(re.finditer(pattern, text))
    for match in matches:
        if match.start() > last:
            yield text[last : match.start()], None
        assert (
            match.lastgroup
        ), f"match should have a lastgroup(check pattern: {pattern})"
        yield match.group(match.lastgroup), match.lastgroup
        last = match.end()
    if last < len(text):
        yield text[last:], None


def lex(
    tokens: list[tuple[str, str | None]], text_types: dict[str | None, TextType]
) -> list[TextNode]:
    return [
        TextNode(
            text,
            text_types.get(tag, TextType.PLAIN),
        )
        for (text, tag) in tokens
    ]


def render(tokens: list[TextNode], render_func: Callable[[TextNode], str]) -> str:
    return "".join(render_func(token) for token in tokens)
