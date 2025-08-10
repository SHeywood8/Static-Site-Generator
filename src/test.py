from main import *
from textnode import TextNode, TextType
from blocktype import *
from markdown_to_html_node import *

import re

def test():
    return
    md = """
>this is a quote
>**hopefully**
>_atleast_
    """

    node = markdown_to_html_node(md)
    print(node.to_html())

test()