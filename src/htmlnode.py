from typing import Optional


class HTMLNode:
    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[list["HTMLNode"]] = None,
        props: dict[str, str] = {},
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
