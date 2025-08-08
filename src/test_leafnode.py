import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_children(self):
        node = LeafNode("b", "This should be bold!")
        self.assertEqual(node.to_html(), "<b>This should be bold!</b>")