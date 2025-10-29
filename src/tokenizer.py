import re


def tokenize(text, delimiters):
    delmiters = "|".join(re.escape(d) for d in delimiters)
    pattern = f"({delmiters})"
    return re.split(pattern, text)
