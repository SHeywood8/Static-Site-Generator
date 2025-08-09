import unittest

from textnode import TextNode, TextType
from main import split_nodes_delimiter

class TestNodeSplitterNode(unittest.TestCase):
    def test_multiple_splits(self):
        node = TextNode("This is some **text** with two **bolds**!", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes.__repr__(), '[TextNode("This is some ", TextType.TEXT), TextNode("text", TextType.BOLD), TextNode(" with two ", TextType.TEXT), TextNode("bolds", TextType.BOLD), TextNode("!", TextType.TEXT)]')
    
    def test_split_ends(self):
        node = TextNode("_This_ text is italic at the start and _end!_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes.__repr__(), '[TextNode("This", TextType.ITALIC), TextNode(" text is italic at the start and ", TextType.TEXT), TextNode("end!", TextType.ITALIC)]')
    
    def test_multiple_nodes_with_different_styles(self):
        node1 = TextNode("This is some **text** with two **bolds**!", TextType.TEXT)
        node2 = TextNode("_This_ text is italic at the start and _end!_", TextType.TEXT)
        new_nodes1 = split_nodes_delimiter([node1, node2], "**", TextType.BOLD)
        new_nodes2 = split_nodes_delimiter([node1, node2], "_", TextType.BOLD)
        self.assertEqual(new_nodes1.__repr__(), 
        '[TextNode("This is some ", TextType.TEXT), TextNode("text", TextType.BOLD), TextNode(" with two ", TextType.TEXT), TextNode("bolds", TextType.BOLD), TextNode("!", TextType.TEXT), TextNode("_This_ text is italic at the start and _end!_", TextType.TEXT)]'
        )
        self.assertEqual(new_nodes2.__repr__(),
        '[TextNode("This is some **text** with two **bolds**!", TextType.TEXT), TextNode("This", TextType.BOLD), TextNode(" text is italic at the start and ", TextType.TEXT), TextNode("end!", TextType.BOLD)]'
        )