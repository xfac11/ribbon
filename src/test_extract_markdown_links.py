import unittest
from extractmarkdownlinks import extract_markdown_links

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_with_image(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)
    
    def test_with_link(self):
        matches = extract_markdown_links(
            "This is text with an [google](https://google.com)"
        )
        self.assertListEqual([("google", "https://google.com")], matches)
    

    def test_multiple_links(self):
        matches = extract_markdown_links(
            "This is text with an [google](https://google.com) and a link to [youtube](https://youtube.com)"
        )
        self.assertListEqual([("google", "https://google.com"), ("youtube", "https://youtube.com")], matches)
    
    def test_multiple_links_and_images(self):
        matches = extract_markdown_links(
            "This is text with an [google](https://google.com) and a link to [youtube](https://youtube.com) and with some pictures ![image](images/jump.png)"
        )
        self.assertListEqual([("google", "https://google.com"), ("youtube", "https://youtube.com")], matches)

    def test_multiple_links_and_images_2(self):
        matches = extract_markdown_links(
            "This is text with an [google](https://google.com) and a link to [youtube](https://youtube.com) and with some pictures ![image](images/jump.png)" \
            "and even more stuff [boot.dev](https://boot.dev) ![boots](images/boots.jpeg)"
        )
        self.assertListEqual([("google", "https://google.com"), ("youtube", "https://youtube.com"), ("boot.dev", "https://boot.dev")], matches)
    
    def test_broken_links(self):
        matches = extract_markdown_links(
            "(wasd)[ds]"
        )
        self.assertListEqual([], matches)

    def test_broken_and_good_links(self):
        matches = extract_markdown_links(
            "(wasd)[ds] [Space marine 2](https://spacemarine2.com)"
        )
        self.assertListEqual([("Space marine 2", "https://spacemarine2.com")], matches)