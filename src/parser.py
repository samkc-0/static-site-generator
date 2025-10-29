from lexer import lex
from textnode import TextNode, TextType
from tokenizer import tokenize


def lex_node(text_node: TextNode, token_map: dict[str, TextType]):
    tokens = tokenize(text_node.text, token_map.keys())
    return lex(tokens, token_map)


def split_nodes_delimiter(nodes: list[TextNode], delimiter: str, text_type: TextType):
    output = []
    for node in nodes:
        output.extend(lex_node(node, {delimiter: text_type}))
    return output
