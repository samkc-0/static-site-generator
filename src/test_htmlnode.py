from htmlnode import HTMLNode
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
