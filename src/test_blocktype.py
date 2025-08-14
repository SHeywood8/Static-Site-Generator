import unittest

from split_nodes import *
from blocktype import *

class TestBlockType(unittest.TestCase):
    def test_heading(self):
        h1 = "# This is heading 1"
        h2 = "## This is heading 2"
        h3 = "### This is heading 3"
        h4 = "#### This is heading 4"
        h5 = "##### This is heading 5"
        h6 = "###### This is heading 6"
        h7 = "####### This has too many hashtags"
        h11 = "########### This does too"
        for heading in [h1, h2, h3, h4, h5, h6]:
            self.assertEqual(block_to_block_type(heading), BlockType.HEADING)
        for heading in [h7, h11]:
            self.assertEqual(block_to_block_type(heading), BlockType.PARAGRAPH)
    
    def test_code(self):
        code = "```this is a code block```"
        not_code = "```this is not"
        not_code2 = "neither is this```"
        self.assertEqual(block_to_block_type(code), BlockType.CODE)
        for c in [not_code, not_code2]:
            self.assertEqual(block_to_block_type(c), BlockType.PARAGRAPH)
    
    def test_quote(self):
        goods = [
            ">how's it going",
            ">hi\n>hello\n>howdy!"
        ]
        bads = [
            ">this want's to be a quote\nbut isn't",
            ">this does too\nbut again\n>is not"
        ]
        for m in goods:
            self.assertEqual(block_to_block_type(m), BlockType.QUOTE)
        for m in bads:
            self.assertEqual(block_to_block_type(m), BlockType.PARAGRAPH)
    
    def test_unordered_list(self):
        goods = [
            "- item1\n- item2",
            "- hi"
        ]
        bads = [
            "- item1\nitem2",
            "- item1\nitem2\n- item3"
        ]
        for m in goods:
            self.assertEqual(block_to_block_type(m), BlockType.UNORDERED_LIST)
        for m in bads:
            self.assertEqual(block_to_block_type(m), BlockType.PARAGRAPH)
    
    def test_ordered_list(self):
        goods = [
            "1. item1\n2. item2",
            "1. hi"
        ]
        bads = [
            "1.item1\nitem2",
            "2.item1\nitem2\n3.item3"
        ]
        for m in goods:
            self.assertEqual(block_to_block_type(m), BlockType.ORDERED_LIST)
        for m in bads:
            self.assertEqual(block_to_block_type(m), BlockType.PARAGRAPH)