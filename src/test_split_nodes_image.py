import unittest
from splitnodesimage import split_nodes_image
from textnode import*
class TestSplitNodesImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_non_images(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)", TextType.PLAIN),
            ],
            new_nodes,
        )
    
    def test_split_only_image(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes
        )
    
    def test_split_image_with_text_after_end_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) with some more ![third image](images/profile.png) and some more text",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" with some more ", TextType.PLAIN),
                TextNode(
                    "third image", TextType.IMAGE, "images/profile.png"
                ),
                TextNode(" and some more text", TextType.PLAIN),
            ],
            new_nodes,
        )
    
    def test_split_images_two_images_only(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)![image2](image2.png)",
            TextType.PLAIN
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("image2", TextType.IMAGE, "image2.png"),
            ],
            new_nodes
        )
    
    def test_split_images_empty_list(self):
        new_nodes = split_nodes_image([])
        self.assertListEqual(new_nodes, [])
    
    def test_split_images_with_images_already(self):
        nodes = [
                TextNode(
                    "![image](https://i.imgur.com/zjjcJKZ.png) and some text here ![image2](image2.png)",
                    TextType.PLAIN
                ),
                TextNode(
                    "image", TextType.IMAGE, "image.png"
                ),
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and some text here ", TextType.PLAIN),
                TextNode("image2", TextType.IMAGE, "image2.png"),
                TextNode("image", TextType.IMAGE, "image.png"),
            ],
            new_nodes
        )
    

    def test_split_images_with_nodes_already(self):
        nodes = [
                TextNode("![image](https://i.imgur.com/zjjcJKZ.png) and some text here ![image2](image2.png)",TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "image.png"),
                TextNode("![pubg](pubg.com) where the game is", TextType.PLAIN),
                TextNode("bold", TextType.BOLD),
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and some text here ", TextType.PLAIN),
                TextNode("image2", TextType.IMAGE, "image2.png"),
                TextNode("image", TextType.IMAGE, "image.png"),
                TextNode("pubg", TextType.IMAGE, "pubg.com"),
                TextNode(" where the game is", TextType.PLAIN),
                TextNode("bold", TextType.BOLD)
            ],
            new_nodes
        )

        
