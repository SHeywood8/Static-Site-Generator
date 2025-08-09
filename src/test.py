from main import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

import re

def test():
    text = 'This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)'
    print(extract_markdown_images(text))
    text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text2))

test()