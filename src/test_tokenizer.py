import re
import pytest
from tokenizer import tokenize


def test_re_split():
    assert re.split(f"({re.escape('**')})", "this is **bold**") == [
        "this is ",
        "**",
        "bold",
        "**",
        "",
    ]


def test_tokenize():
    assert tokenize("this is **bold** and this is _italic_.", ["**", "_"]) == [
        "this is ",
        "**",
        "bold",
        "**",
        " and this is ",
        "_",
        "italic",
        "_",
        ".",
    ]
