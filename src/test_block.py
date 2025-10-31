import pytest
from block import BlockType, block_to_block_type
from helpers import md_to_blocks


def test_markdown_to_blocks():
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
    blocks = md_to_blocks(md)
    assert blocks == [
        "This is **bolded** paragraph",
        "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
        "- This is a list\n- with items",
    ]


@pytest.mark.parametrize(
    "block, want",
    [
        ("# h1", BlockType.HEADING),
        ("## h2", BlockType.HEADING),
        ("### h3", BlockType.HEADING),
        ("#### h4", BlockType.HEADING),
        ("##### h5", BlockType.HEADING),
        ("###### h6", BlockType.HEADING),
        ("###### h6 with spaces", BlockType.HEADING),
        ("####### not a heading", BlockType.PARAGRAPH),
        ("```import pytest\nfrom block import BlockType\n```", BlockType.CODE),
        ("> it was the best of times it was the worst of times", BlockType.QUOTE),
        ("- groceries\n- homework\n- cleaning", BlockType.UNORDERED_LIST),
        ("-groceries\n-homework\n-cleaning", BlockType.PARAGRAPH),
        ("1. beethoven\n2. tchaikovsky\n3. mozart", BlockType.ORDERED_LIST),
        ("1.beethoven\n2.tchaikovsky\n3.mozart", BlockType.PARAGRAPH),
        ("0. beethoven\n1. tchaikovsky\n2. mozart", BlockType.PARAGRAPH),
        ("1. beethoven\n3. tchaikovsky\n3. mozart", BlockType.PARAGRAPH),
    ],
)
def test_block_to_block_type(block, want):
    got = block_to_block_type(block)
    assert got == want
