from typing import Optional

Props = dict[str, str]


class HTMLNode:
    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[list["HTMLNode"]] = None,
        props: Props = {},
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError

    def props_to_html(self) -> str:
        return "".join(f' {k}="{v}"' for k, v in self.props.items())

    def __repr__(self) -> str:
        child_count = (
            "[" + f"({len(self.children)} children)..." + "]"
            if self.children
            else "None"
        )
        prop_count = (
            "{" + f"({len(self.props)} props)..." + "}" if len(self.props) else "{}"
        )
        return f"HTMLNode(tag='{self.tag}', value='{self.value}', children={child_count}, props={prop_count})"


class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: Props = {}):
        if value is None:
            raise ValueError("LeafNode must have a value, but got value=None")
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.tag is None:
            return str(self.value)
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: Props = {}):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("ParentNode must have a tag, but got tag=None")
        if self.children is None:
            raise ValueError("ParentNode must have child nodes, but got children=None")
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
