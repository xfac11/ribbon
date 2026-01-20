import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("This is important text", TextType.BOLD)
        node2 = TextNode("This is fabolous text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_texttype_not_eq(self):
        node = TextNode("This is important", TextType.ITALIC)
        node2 = TextNode("This is important", TextType.PLAIN)
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("Text", TextType.CODE, "github.com")
        node2 = TextNode("Text", TextType.CODE, "github.com")
        self.assertEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("Text", TextType.LINK, "youtube.com")
        node2 = TextNode("Text", TextType.LINK, "google.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
