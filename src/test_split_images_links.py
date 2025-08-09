import unittest
from main import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestSplitImageNode(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_multiple_links(self):
        node = TextNode(
            "This is [text](https://youtube.com) with [multiple](https://xkcd.com) [links](https://youtube.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.LINK, "https://youtube.com"),
                TextNode(" with ", TextType.TEXT),
                TextNode("multiple", TextType.LINK, "https://xkcd.com"),
                TextNode(" ", TextType.TEXT),
                TextNode("links", TextType.LINK, "https://youtube.com")
            ],
            new_nodes,
        )
    
    def test_image_and_link(self):
        node = TextNode(
            "This is text with a [link](https://youtube.com) and an ![image](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.TEXT
        )