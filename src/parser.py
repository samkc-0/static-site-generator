from typing import Callable, Generator
from functools import partial
from textnode import TextNode, TextType
import re


def make_pattern(symbol: str, text_type: TextType):
    pattern = str(re.escape(symbol))
    return pattern + "(?P<" + text_type.value + ">.*?)" + pattern


bold_pattern = make_pattern("**", TextType.BOLD)
italic_pattern = make_pattern("_", TextType.ITALIC)
code_pattern = make_pattern("`", TextType.CODE)
link_pattern = r"(?<!\!)" + r"(?P<" + TextType.LINK.value + r">\[.*?\]\(.*?\))"
image_pattern = r"(?P<" + TextType.IMAGE.value + r">!\[.*?\]\(.*?\))"

PATTERNS = [bold_pattern, italic_pattern, code_pattern, image_pattern, link_pattern]


def parse_link(raw: str, text_type: TextType) -> TextNode:
    text = raw[raw.find("[") + 1 : raw.find("]")]
    url = raw[raw.find("(") + 1 : raw.find(")")]
    return TextNode(text, text_type, url)


PARSERS = {
    TextType.PLAIN.value: partial(TextNode, text_type=TextType.PLAIN),
    TextType.BOLD.value: partial(TextNode, text_type=TextType.BOLD),
    TextType.ITALIC.value: partial(TextNode, text_type=TextType.ITALIC),
    TextType.CODE.value: partial(TextNode, text_type=TextType.CODE),
    TextType.LINK.value: partial(parse_link, text_type=TextType.LINK),
    TextType.IMAGE.value: partial(parse_link, text_type=TextType.IMAGE),
}


def get_text_type(text_type: str) -> TextType:
    return TextType(text_type)


def tokenize(text, patterns=PATTERNS) -> Generator:
    """
    Tokenizes a string into a list of tuples (text, tag).
    """
    pattern = re.compile("|".join(patterns))
    last = 0
    matches = list(re.finditer(pattern, text))
    for match in matches:
        if match.start() > last:
            yield text[last : match.start()], TextType.PLAIN.value
        assert (
            match.lastgroup
        ), f"match should have a lastgroup(check pattern: {pattern})"
        yield match.group(match.lastgroup), match.lastgroup
        last = match.end()
    if last < len(text):
        yield text[last:], TextType.PLAIN.value


def lex(
    tokens: list[tuple[str, str]], parsers: dict[str, Callable] = PARSERS
) -> Generator:
    """
    Lexes a list of tokens into a list of TextNodes.
    """
    for text, tag in tokens:
        yield parsers[tag](text)


def render(tokens: list[TextNode], render_func: Callable[[TextNode], str]) -> str:
    return "".join(render_func(token) for token in tokens)
