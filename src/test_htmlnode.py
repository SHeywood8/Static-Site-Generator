import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test1(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props = props)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
        #print(node)
        #print(node.props_to_html())
    
    def test2(self):
        node = HTMLNode(tag = "h1", value = "This is a heading!")
        #print(node)
        self.assertEqual(node.__repr__(), "HTMLNode(tag = h1, value = This is a heading!)")
    
    def test3(self):
        node1 = HTMLNode(value = "This is a child")
        node2 = HTMLNode(value = "This is a parent", children = [node1])
        #print(node2)
        self.assertEqual(node2.__repr__(), "HTMLNode(value = This is a parent, children = [HTMLNode(value = This is a child)])")

