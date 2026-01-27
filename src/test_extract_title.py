import unittest
from extracttitle import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_hello(self):
        md = "# Hello"
        title = extract_title(md)
        self.assertEqual("Hello", title)
    
    def test_nothing(self):
        md = ""
        self.assertRaises(Exception, extract_title, md)
    
    def test_leading_whitespace(self):
        md = "#      Frodo\nSomeone with more than a title"
        title = extract_title(md)
        self.assertEqual("Frodo", title)
    
    def test_trailing_whitespace(self):
        md = "#      Frodo       \nSomeone with more than a title"
        title = extract_title(md)
        self.assertEqual("Frodo", title)
    
    def test_header_two(self):
        md = "##      Frodo\nSomeone with more than a title"
        self.assertRaises(Exception, extract_title, md)

