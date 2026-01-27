from markdowntohtmlnode import markdown_to_html_node
import unittest

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    
    def test_heading(self):
        md = """
# Heading with some words

And another **paragraph**
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, 
            "<div><h1>Heading with some words</h1><p>And another <b>paragraph</b></p></div>"
        )
    
    def test_unordered_list(self):
        md = """
- One item
- Second _italic_
- Third **bold**
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>One item</li><li>Second <i>italic</i></li><li>Third <b>bold</b></li></ul></div>"
        )
    
    def test_ordered_list(self):
        md = """
1. First **item**
2. Second item
3. Third _item_
4. Fourth item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First <b>item</b></li><li>Second item</li><li>Third <i>item</i></li><li>Fourth item</li></ol></div>"
        )
    

    def test_quote(self):
        md = """
> Markdown is often used to format readme files, **for** writing messages in online discussion forums, and to create rich text using a plain text editor.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Markdown is often used to format readme files, <b>for</b> writing messages in online discussion forums, and to create rich text using a plain text editor.</blockquote></div>"
        )
    
    def test_multiple_blocks(self):
        md = """
# Markdown syntax guide

## Headers

# This is a Heading h1

## This is a Heading h2

###### This is a Heading h6

## Emphasis

You may be using ![Markdown Live Preview](https://markdownlivepreview.com/image/Markdown-mark.svg).
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h1>Markdown syntax guide</h1><h2>Headers</h2><h1>This is a Heading h1</h1><h2>This is a Heading h2</h2><h6>This is a Heading h6</h6><h2>Emphasis</h2><p>You may be using <img src="https://markdownlivepreview.com/image/Markdown-mark.svg" alt="Markdown Live Preview"></img>.</p></div>'
        )