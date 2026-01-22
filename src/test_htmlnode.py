import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_node_creation(self):
        node = HTMLNode(tag="p")
        self.assertEqual(node.tag, "p")
    
    def test_node_multiple_creation(self):
        node = HTMLNode(value="Hello world", tag="p")
        node2 = HTMLNode(props={"href": "https://www.google.com"}, tag="a", value="Link to google")
        node3 = HTMLNode(tag="h1", children=[node, node2])
        self.assertIn(node, node3.children)
    
    def test_props_to_html(self):
        node = HTMLNode(value="Hello internet", tag="h1")
        node3 = HTMLNode(
            tag="a",
            value="Link to google",
            props=
            {
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        nodeParent = HTMLNode(tag="p", children=[node, node3], value="TM")
        html_props = node3.props_to_html()
        self.assertEqual(html_props, ' href="https://www.google.com" target="_blank"')
    
    def test_repr(self):
        node = HTMLNode(tag="h2", value="My website")
        represent = node.__repr__()
        self.assertEqual(represent, "HTMLNode(h2, My website, None, None)")

    def test_to_html(self):
        node = HTMLNode(tag="p", value="Hello")
        self.assertRaises(NotImplementedError, node.to_html)
        
