from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def md_to_blocks(text: str) -> list[str]:
    return [line.strip() for line in text.split("\n\n")]


def block_to_block_type(block: str) -> BlockType:
    if matches(r"^#{1,6} .*?$", block):
        return BlockType.HEADING
    if re.match(r"```.*?```", block, re.DOTALL):
        return BlockType.CODE
    if matches(r"> .*?", block):
        return BlockType.QUOTE
    if matches(r"^- .*?$", block):
        return BlockType.UNORDERED_LIST
    if is_ordered_list(block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def matches(pattern, block):
    return all(re.match(pattern, line) for line in block.split("\n"))


def is_ordered_list(block: str):
    for i, line in enumerate(block.split("\n"), 1):
        m = re.match(r"^(?P<count>\d+)\. .*?$", line)
        if not m:
            return False
        count = m.groupdict().get("count", False)
        if (not count) or (int(count) != i):
            return False
    return True
