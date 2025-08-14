from copy_dir import clear_dir, copy_dir
from generate_page import generate_page, generate_dir
from split_nodes import split_nodes_image, text_to_textnodes
from textnode import TextNode, TextType
from markdown_to_html_node import text_to_children, markdown_to_html_node

def main():
    clear_dir("public")
    copy_dir("static", "public")
    generate_dir("content", "template.html", "public")
    

main()