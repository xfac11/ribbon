import unittest
from splitnodesdelimiter import split_nodes_delimiter
from textnode import*
class TestSplitNodesDelimiter(unittest.TestCase):
    def test_one_bold_phrase(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("bolded phrase", TextType.BOLD),
                TextNode(" in the middle", TextType.PLAIN),
            ]
        )
    
    def test_two_bold_phrases(self):
        node = TextNode("This is text with a **bolded phrase** in the middle and one **at the end**", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("bolded phrase", TextType.BOLD),
                TextNode(" in the middle and one ", TextType.PLAIN),
                TextNode("at the end", TextType.BOLD),
            ]
        )
    
    def test_two_bold_and_code(self):
        node = TextNode("This is text with a **bolded phrase** in the middle and one `code at the end`", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("bolded phrase", TextType.BOLD),
                TextNode(" in the middle and one ", TextType.PLAIN),
                TextNode("code at the end", TextType.CODE),
            ]
        )
    
    def test_syntax_error(self):
        node = TextNode("This is text with a _italic phrase_ in the middle and one `code at the end", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertRaises(SyntaxError, split_nodes_delimiter, new_nodes, "`", TextType.CODE)
    
    def test_multiple_delimiters(self):
        node = TextNode("This is _text_ with a **bolded phrase** in the **middle** and one `code at the end`", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.PLAIN),
                TextNode("text", TextType.ITALIC),
                TextNode(" with a ", TextType.PLAIN),
                TextNode("bolded phrase", TextType.BOLD),
                TextNode(" in the ", TextType.PLAIN),
                TextNode("middle", TextType.BOLD),
                TextNode(" and one ", TextType.PLAIN),
                TextNode("code at the end", TextType.CODE),
            ]
        )
    
    def test_only_bold_phrase(self):
        node = TextNode("**Bold Text**", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("Bold Text", TextType.BOLD),
            ]
        )
    
    def test_only_italic_phrase(self):
        node = TextNode("_Italic Text_", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("Italic Text", TextType.ITALIC),
            ]
        )
    
    def test_different_texttype_delimiter(self):
        node = TextNode("_Italic Text_", TextType.PLAIN)
        self.assertRaises(ValueError, split_nodes_delimiter, [node], "**", TextType.ITALIC)
