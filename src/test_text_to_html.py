import unittest

from htmlnode import ParentNode, LeafNode, HTMLNode
from textnode import TextNode, TextType
from main import text_node_to_html_node

class TestTextToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")