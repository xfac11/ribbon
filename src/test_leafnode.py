import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        print(f"Test with Node: {node}")
        print("Expecting equal to <p>Hello, world!</p>")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        print("Succes")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        print(f"Test with Node: {node}")
        print('Expecting equal to <a href="https://www.google.com">Click me!</a>')
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
        print("Succes")

    def test_leaf_to_html_value_none(self):
        node = LeafNode("p", None)
        print(f"Test with Node: {node}")
        print("Expecting a value error when calling to_html")
        self.assertRaises(ValueError, node.to_html)
        print("Succes")
    

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello World")
        print(f"Test with Node: {node}")
        print("Expecting equal to <h1>Hello World</h1>")
        self.assertEqual(node.to_html(), "<h1>Hello World</h1>")
        print("Succes")