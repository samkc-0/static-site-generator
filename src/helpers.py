from block import block_to_block_type, BlockType
from parser import parse
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType


def md_to_blocks(text: str) -> list[str]:
    return [line.strip() for line in text.split("\n\n")]


def md_to_html_node(text: str):
    blocks = [(block, block_to_block_type(block)) for block in md_to_blocks(text)]
    print(blocks)
    document = []
    for block, block_type in blocks:
        if block == "":
            continue
        match block_type:
            case BlockType.PARAGRAPH:
                text_nodes = parse(block)
                leaf_nodes = [text_node_to_html_node(t) for t in text_nodes]
                parent_node = ParentNode("p", leaf_nodes)
                document.append(parent_node)
            case BlockType.HEADING:
                # is it h1, h2, h3, h4, h5, h6
                h, text = get_heading_type(block)
                text_nodes = parse(text)
                leaf_nodes = [text_node_to_html_node(t) for t in text_nodes]
                document.append(ParentNode(h, leaf_nodes))
            case BlockType.CODE:
                code = LeafNode("code", block.strip("```"))
                pre = ParentNode("pre", [code])
                document.append(pre)
            case BlockType.QUOTE:
                _, text = block.split(" ", 1)
                document.append(LeafNode("blockquote", text))
            case BlockType.UNORDERED_LIST:
                ul = list_block_to_html_node(block, "ul")
                document.append(ul)
            case BlockType.ORDERED_LIST:
                ol = list_block_to_html_node(block, "ol")
                document.append(ol)
    return ParentNode("div", document)


def list_block_to_html_node(block: str, tag: str):
    lines_without_numbers = [line.split(" ", 1)[1] for line in block.split("\n")]
    text_nodes = [parse(line) for line in lines_without_numbers]
    children = []
    for line in text_nodes:
        li = ParentNode("li", [text_node_to_html_node(t) for t in line])
        children.append(li)
    list_node = ParentNode(tag, children)
    return list_node


def get_heading_type(heading_md: str):
    hashtags, text = heading_md.split(" ", 1)
    assert all(c == "#" for c in hashtags), f"'{heading_md}' is not a valid heading"
    assert (
        len(hashtags) <= 6 and len(hashtags) >= 1
    ), f"'heading {heading_md}' has wrong number of '#'"
    return f"h{len(hashtags)}", text


def text_node_to_html_node(text_node: TextNode) -> HTMLNode:
    match text_node.text_type:
        case TextType.PLAIN:
            return LeafNode(None, text_node.text)

        case TextType.BOLD:
            return LeafNode("b", text_node.text)

        case TextType.ITALIC:
            return LeafNode("i", text_node.text)

        case TextType.CODE:
            return LeafNode("code", text_node.text)

        case TextType.LINK:
            if text_node.url is None:
                return LeafNode("a", text_node.text)
            return LeafNode("a", text_node.text, {"href": text_node.url})

        case TextType.IMAGE:
            if text_node.url is None:
                return LeafNode("img", "", {"alt": text_node.text})
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
