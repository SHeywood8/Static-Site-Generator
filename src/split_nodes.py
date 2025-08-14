from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from blocktype import BlockType, block_to_block_type
import re

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

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        text = old_node.text
        matches = extract_markdown_images(text)
        if matches == []:
            new_nodes.append(old_node)
        else:
            text_to_edit = text
            for match in matches:
                match_string = f"![{match[0]}]({match[1]})"
                parts = text_to_edit.split(match_string)
                if parts[0] != '':
                    new_nodes.append(TextNode(parts[0], TextType.TEXT))
                new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
                text_to_edit = match_string.join(parts[1:])
            if text_to_edit != '':
                new_nodes.append(TextNode(text_to_edit, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        text = old_node.text
        matches = extract_markdown_links(text)
        if matches == []:
            new_nodes.append(old_node)
        else:
            text_to_edit = text
            for match in matches:
                match_string = f"[{match[0]}]({match[1]})"
                parts = text_to_edit.split(match_string)
                if parts[0] != '':
                    new_nodes.append(TextNode(parts[0], TextType.TEXT))
                new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))
                text_to_edit = match_string.join(parts[1:])
            if text_to_edit != '':
                        new_nodes.append(TextNode(text_to_edit, TextType.TEXT))
    return new_nodes

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

def extract_markdown_images(text):
    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes

def markdown_to_blocks(markdown):
    blocks = markdown.strip().strip("\n").split("\n\n")
    for i in range(len(blocks)):
        blocks[i].strip()
        if blocks[i] == '':
            blocks.remove(blocks[i])
    return blocks