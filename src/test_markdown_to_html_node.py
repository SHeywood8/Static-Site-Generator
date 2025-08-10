import unittest

from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_one_of_each(self):
        md = '''
##### This is a **large** markdown block!

The goal is to test each and every different block type in _one_ go!

The types are:

- unordered list
- which is what this is

1. ordered list
2. which is what this is

>quotes
>which is what this is

```
code
which is what this is
```

And just a plain ol' paragraph which we've now got _three_ of! Isn't `that` crazy?
'''
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h0>This is a <b>large</b> markdown block!</h0><p>The goal is to test each and every different block type in <i>one</i> go!</p><p>The types are:</p><ul><li>unordered list</li><li>which is what this is</li></ul><ol><li>ordered list</li><li>which is what this is</li></ol><blockquote>quotes\nwhich is what this is</blockquote><pre><code>code\nwhich is what this is\n</code></pre><p>And just a plain ol' paragraph which we've now got <i>three</i> of! Isn't <code>that</code> crazy?</p></div>"
        )