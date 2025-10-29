import re
from textnode import TextNode, TextType
import tokenizer

TOKEN_MAP = {"**": TextType.BOLD, "_": TextType.ITALIC, "`": TextType.CODE}


def lex(tokens: list[str], token_map: dict[str, TextType] = TOKEN_MAP):
    nodes = []
    i = 0
    while i < len(tokens):
        if i >= len(tokens):
            break
        token = tokens[i]
        if token in TOKEN_MAP and tokens[i + 2] == token:
            text_node = TextNode(tokens[i + 1], TOKEN_MAP[token])
            nodes.append(text_node)
            i += 3
        else:
            text_node = TextNode(token, TextType.PLAIN)
            nodes.append(text_node)
            i += 1
    return nodes
