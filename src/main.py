from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
import re

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

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if (delimiter not in old_node.text
            or old_node.text_type is not TextType.TEXT
            ):
            new_nodes.append(old_node)
        else:
            node_text = old_node.text
            parts = node_text.split(delimiter)
            if len(parts) % 2 == 0:
                raise Exception ("Invalid markdown")
            for i in range(len(parts)):
                if i % 2 == 0:
                    if parts[i] == '':
                        continue
                    new_nodes.append(TextNode(parts[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(parts[i], text_type))
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


main()