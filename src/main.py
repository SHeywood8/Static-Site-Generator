from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    pass

def text_node_to_html_node(text_node):
    text = text_node.text
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag = None, value = text)
        case TextType.BOLD:
            return LeafNode(tag = "b", value = text)
        case TextType.ITALIC:
            return LeafNode(tag = 'i', value = text)
        case TextType.CODE:
            return LeafNode(tag = 'code', value = text)
        case TextType.LINK:
            return LeafNode(tag = 'a', value = text, props = {"href" : text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag = 'img', value = '', props = {
                "src" : text_node.url,
                "alt" : text
            })

main()
