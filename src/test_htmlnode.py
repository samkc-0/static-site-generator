from htmlnode import HTMLNode, LeafNode, ParentNode
import pytest


def test_htmlnode_repr_empty_children_and_props():
    node = HTMLNode("div", "Hello")
    assert repr(node) == "HTMLNode(tag='div', value='Hello', children=None, props={})"


def test_htmlnode_repr_with_children():
    node = HTMLNode("div", "Hello", [HTMLNode("span", "World")])
    assert (
        repr(node)
        == "HTMLNode(tag='div', value='Hello', children=[(1 children)...], props={})"
    )


def test_htmlnode_repr_with_props():
    node = HTMLNode("div", "Hello", props={"class": "my-class"})
    assert (
        repr(node)
        == "HTMLNode(tag='div', value='Hello', children=None, props={(1 props)...})"
    )


def test_leaf_to_html_p():
    node = LeafNode("p", "Hello, world!")
    assert node.to_html() == "<p>Hello, world!</p>"


def test_leaf_requires_value():
    with pytest.raises(ValueError):
        node = LeafNode("p", None)


def test_leaf_without_tag_returns_str():
    node = LeafNode(None, "Click me")
    assert node.to_html() == "Click me"


def test_parent_node_recursion():
    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    want = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
    assert node.to_html() == want, f"got {node.to_html()}, want {want}"


def test_to_html_with_children():
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    assert parent_node.to_html() == "<div><span>child</span></div>"


def test_to_html_with_grandchildren():
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    assert parent_node.to_html() == "<div><span><b>grandchild</b></span></div>"
