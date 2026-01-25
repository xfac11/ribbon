import unittest
from extractmarkdownimages import extract_markdown_images

class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_images_with_links(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and some links [link1](link.com) and some more ![Happy] haha no but this one [youtube](youtube.com)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image](https://i.imgur.com/FKqOBIR.jpeg) and one last ![third image](https://i.imgur.com/ZXCc3b9.jpeg)"
        )
        self.assertListEqual(
            [
                ("image", "https://i.imgur.com/zjjcJKZ.png"),
                ("image", "https://i.imgur.com/FKqOBIR.jpeg"),
                ("third image", "https://i.imgur.com/ZXCc3b9.jpeg")
            ], matches
        )
    

    def test_broken_and_good_links(self):
        matches = extract_markdown_images(
            "(wasd)[ds] ![Space marine 2](https://spacemarine2.com)"
        )
        self.assertListEqual([("Space marine 2", "https://spacemarine2.com")], matches)
