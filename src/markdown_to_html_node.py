from blocktype import BlockType, block_to_block_type
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextType, TextNode
from split_nodes import text_node_to_html_node, markdown_to_blocks, text_to_textnodes


def markdown_to_html_node(markdown):
    body_node = ParentNode(tag = "div", children = [])
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.QUOTE:
                lines = block.split("\n")
                lines = [line.replace(">", "").strip() for line in lines]
                text = "\n".join(lines)
                block_node = ParentNode(tag = "blockquote", children = text_to_children(text))
            
            case BlockType.UNORDERED_LIST:
                block_node = ParentNode(tag = "ul", children = [])
                lines = block.split("\n")
                for i in range(len(lines)):
                    lines[i] = lines[i][2:]
                for line in lines:
                    line_node = ParentNode(tag = "li", children = text_to_children(line))
                    block_node.children.append(line_node)
            
            case BlockType.ORDERED_LIST:
                block_node = ParentNode(tag = "ol", children = [])
                lines = block.split("\n")
                for i in range(len(lines)):
                    if lines[i][2] == " ":
                        lines[i] = lines[i][3:]
                    else:
                        lines[i] = lines[i][2:]
                for line in lines:
                    line_node = ParentNode(tag = "li", children = text_to_children(line))
                    block_node.children.append(line_node)
            
            case BlockType.CODE:
                block_node = ParentNode(tag = "pre", children = [])
                text = block.strip("```").lstrip("\n")
                text_node = TextNode(text, TextType.CODE)
                html_node = text_node_to_html_node(text_node)
                block_node.children.append(html_node)
            
            case BlockType.HEADING:
                count = 0
                for char in markdown:
                    if char == "#":
                        count += 1
                    else:
                        break
                text = block.strip(r"#{1,6} ")
                block_node = ParentNode(tag = f"h{count}", children = text_to_children(text))
            
            case BlockType.PARAGRAPH:
                text = " ".join(block.split("\n"))
                block_node = ParentNode(tag = "p", children = text_to_children(text))

            
        body_node.children.append(block_node)
    return body_node



def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes