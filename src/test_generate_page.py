from generate_page import extract_title


def test_extract_title():
    assert extract_title("# This is a title") == "This is a title"
    assert (
        extract_title("this is not the title\n# but this is\n## and this is not")
        == "but this is"
    )
