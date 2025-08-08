import unittest

from htmlnode import ParentNode, LeafNode, HTMLNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_multiple_children(self):
        child1 = LeafNode("b", "child1")
        child2 = LeafNode("span", "child2")
        grandchild = LeafNode("div", "grandchild")
        child3 = ParentNode("i", [grandchild])
        parent = ParentNode("p", [child1, child2, child3])
        self.assertEqual(
            parent.to_html(),
            "<p><b>child1</b><span>child2</span><i><div>grandchild</div></i></p>"
        )