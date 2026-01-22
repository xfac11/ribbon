import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        print(grandchild_node, child_node, parent_node)
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_no_children(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("div", [])
        parent_node = ParentNode("div", [child_node], {"className": "wrapper"})
        print(grandchild_node, child_node, parent_node)
        self.assertRaises(ValueError, parent_node.to_html)

    def test_no_tag(self):
        child_node = LeafNode("p", "child")
        parent_node = ParentNode(None, [child_node])
        self.assertRaises(ValueError, parent_node.to_html)
    
    def test_child_no_value(self):
        child_node = LeafNode("div", None)
        parent_node = ParentNode("p", [child_node])
        self.assertRaises(ValueError, parent_node.to_html)

    def test_child_no_tag(self):
        child_node = LeafNode(None, "Hello there I am the child")
        parent_node = ParentNode("h1", [child_node], {"id": "primary-navigation"})
        self.assertEqual(
            parent_node.to_html(),
            '<h1 id="primary-navigation">Hello there I am the child</h1>'
        )
    
    def test_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )
        