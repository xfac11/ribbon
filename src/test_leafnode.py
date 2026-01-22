import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_value_none(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)
    

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello World")
        self.assertEqual(node.to_html(), "<h1>Hello World</h1>")
