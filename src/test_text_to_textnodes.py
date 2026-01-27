import unittest
from texttotextnodes import text_to_textnodes
from textnode import*
class TestTextToTextNodes(unittest.TestCase):
    def test_example(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected_nodes = [
            TextNode("This is ", TextType.PLAIN),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.PLAIN),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(new_nodes, expected_nodes)
    
    def test_no_nodes(self):
        text = "This is just some text"
        expected_nodes = [
            TextNode("This is just some text", TextType.PLAIN),
        ]
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(new_nodes, expected_nodes)
    
    def test_empty_string(self):
        text = ""
        expected_nodes = []
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(new_nodes, expected_nodes)
    
    def test_multiple_nodes(self):
        text = "This is **bold** and one ![image](image.png)"
        expected_nodes = [
            TextNode("This is ",TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
            TextNode(" and one ", TextType.PLAIN),
            TextNode("image", TextType.IMAGE, "image.png"),
        ]
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(new_nodes, expected_nodes)
