from htmlnode import HTMLNode, LeafNode
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
