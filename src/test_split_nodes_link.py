import unittest
from splitnodeslink import split_nodes_link
from textnode import*
class TestSplitNodesLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_non_links(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.PLAIN),
            ],
            new_nodes,
        )
    
    def test_split_only_link(self):
        node = TextNode(
            "[image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes
        )
    
    def test_split_links_with_text_after_end_link(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png) with some more [third image](images/profile.png) and some more text",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" with some more ", TextType.PLAIN),
                TextNode(
                    "third image", TextType.LINK, "images/profile.png"
                ),
                TextNode(" and some more text", TextType.PLAIN),
            ],
            new_nodes,
        )
    
    def test_split_links_two_links_only(self):
        node = TextNode(
            "[image](https://i.imgur.com/zjjcJKZ.png)[image2](image2.png)",
            TextType.PLAIN
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("image2", TextType.LINK, "image2.png"),
            ],
            new_nodes
        )
    
    def test_split_links_empty_list(self):
        new_nodes = split_nodes_link([])
        self.assertListEqual(new_nodes, [])
    
    def test_split_links_with_images_already(self):
        nodes = [
                TextNode(
                    "[image](https://i.imgur.com/zjjcJKZ.png) and some text here [image2](image2.png)",
                    TextType.PLAIN
                ),
                TextNode(
                    "image", TextType.IMAGE, "image.png"
                ),
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertListEqual(
            [
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and some text here ", TextType.PLAIN),
                TextNode("image2", TextType.LINK, "image2.png"),
                TextNode("image", TextType.IMAGE, "image.png"),
            ],
            new_nodes
        )
    

    def test_split_images_with_nodes_already(self):
        nodes = [
                TextNode("[image](https://i.imgur.com/zjjcJKZ.png) and some text here [image2](image2.png)",TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "image.png"),
                TextNode("[pubg](pubg.com) where the game is", TextType.PLAIN),
                TextNode("bold", TextType.BOLD),
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertListEqual(
            [
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and some text here ", TextType.PLAIN),
                TextNode("image2", TextType.LINK, "image2.png"),
                TextNode("image", TextType.IMAGE, "image.png"),
                TextNode("pubg", TextType.LINK, "pubg.com"),
                TextNode(" where the game is", TextType.PLAIN),
                TextNode("bold", TextType.BOLD)
            ],
            new_nodes
        )

    def test_split_links_with_links_already(self):
        nodes = [
                TextNode(
                    "[image](https://i.imgur.com/zjjcJKZ.png) and some text here [image2](image2.png)",
                    TextType.PLAIN
                ),
                TextNode(
                    "image", TextType.LINK, "image.png"
                ),
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertListEqual(
            [
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and some text here ", TextType.PLAIN),
                TextNode("image2", TextType.LINK, "image2.png"),
                TextNode("image", TextType.LINK, "image.png"),
            ],
            new_nodes
        )
    
    def test_split_link_example_from_boot(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.PLAIN,
        )   
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.PLAIN),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.PLAIN),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes
        )
 
