from main import *
from textnode import TextNode, TextType
from blocktype import *

import re

def test():
    markdown = "###### Not a real heading"
    print(block_to_block_type(markdown))

test()