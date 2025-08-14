from copy_dir import clear_dir, copy_dir
from generate_page import generate_page, generate_dir
from split_nodes import split_nodes_image, text_to_textnodes
from textnode import TextNode, TextType
from markdown_to_html_node import text_to_children, markdown_to_html_node
import os, sys

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        basepath = "/"
    else:
        basepath = args[0]
    clear_dir("docs")
    copy_dir("static", "docs")
    generate_dir("content", "template.html", "docs", basepath)
    

main()