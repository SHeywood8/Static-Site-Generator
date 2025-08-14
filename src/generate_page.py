import os, sys
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    abs_from_path = os.path.abspath(from_path)
    abs_template_path = os.path.abspath(template_path)
    abs_dest_path = os.path.abspath(dest_path)
    try:
        with open(abs_from_path, "r") as f:
            content = f.read()
            f.close()
    except:
        raise Exception (f"Error reading file {abs_from_path}")
    try:
        with open(abs_template_path, "r") as f:
            template = f.read()
            f.close()
    except:
        raise Exception (f"Error reading file {abs_template_path}")
    node = markdown_to_html_node(content)
    html_string = node.to_html()
    title = extract_title(content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')
    if not os.path.exists(os.path.dirname(abs_dest_path)):
        print(abs_dest_path)
        print(os.path.dirname(abs_dest_path))
        os.makedirs(os.path.dirname(abs_dest_path))
    with open(abs_dest_path, "w") as f:
        f.write(template)
        f.close()
    
def generate_dir(from_dir, template_path, dest_dir, basepath):
    abs_from_dir = os.path.abspath(from_dir)
    abs_template_path = os.path.abspath(template_path)
    abs_dest_dir = os.path.abspath(dest_dir)
    files = os.listdir(abs_from_dir)
    for file in files:
        new_filepath = os.path.join(abs_from_dir, file)
        if os.path.isfile(new_filepath):
            dest_path = os.path.join(dest_dir, os.path.splitext(file)[0] + ".html")
            generate_page(new_filepath, abs_template_path, dest_path, basepath)
        else:
            os.mkdir(os.path.join(dest_dir, file))
            generate_dir(new_filepath, abs_template_path, os.path.join(dest_dir, file), basepath)