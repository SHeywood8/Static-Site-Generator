from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "PARAGRAPH"
    HEADING = "HEADING"
    CODE = "CODE"
    QUOTE = "QUOTE"
    UNORDERED_LIST = "UNORDERED_LIST"
    ORDERED_LIST = "ORDERED_LIST"

def block_to_block_type(markdown):
    if re.match(r"#{1,6} ", markdown) and re.match("#######", markdown) is None:
        return BlockType.HEADING
    if markdown[0:3] == '```' and markdown[-3:] == '```':
        return BlockType.CODE
    lines = markdown.split("\n")
    is_quote = True
    is_unordered = True
    is_ordered = True
    i = 0
    for line in lines:
        i += 1
        if line[0] != ">":
            is_quote = False
        if line[:2] != "- ":
            is_unordered = False
        if line[:2] != f"{i}.":
            is_ordered = False
    if is_quote:
        return BlockType.QUOTE
    if is_unordered:
        return BlockType.UNORDERED_LIST
    if is_ordered:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH