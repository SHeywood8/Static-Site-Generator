import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_func(self):
        markdown = "# Hello!"
        title = extract_title(markdown)
        self.assertEqual(title, "Hello!")
    
    def test_fail(self):
        markdown = "## Not a title :("
        self.assertRaises(Exception, extract_title, markdown)
    
    def test_func2(self):
        markdown = "This line doesn't have the title\n # This one does!"
        self.assertEqual(extract_title(markdown), "This one does!")