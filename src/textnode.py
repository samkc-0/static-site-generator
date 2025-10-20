from enum import Enum
from typing import Optional, Any


class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: Optional[str] = None):
        if url is not None and text_type not in [TextType.LINK, TextType.IMAGE]:
            raise ValueError("Only links and images can have urls")
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        if self.url is None:
            return f"TextNode(text='{self.text}', text_type={self.text_type})"
        return f"TextNode(text='{self.text}', text_type={self.text_type}, url='{self.url}')"
