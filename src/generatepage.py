from markdowntohtmlnode import markdown_to_html_node
from extracttitle import extract_title
from os import makedirs
import os
def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Tying together a ribbon page from {from_path} to {dest_path} using {template_path}")

    markdown_content = None
    with open(from_path) as f:
        markdown_content = f.read()
    
    template_content = None
    with open(template_path) as f:
        template_content = f.read()
    
    html_string = markdown_to_html_node(markdown_content).to_html()

    title = extract_title(markdown_content)


    full_html_page = template_content.replace("{{ Title }}", title)
    full_html_page = full_html_page.replace("{{ Content }}", html_string)
    full_html_page = full_html_page.replace('href="/', f'href="{base_path}')
    full_html_page = full_html_page.replace('src="/', f'src="{base_path}')
    parent = os.path.dirname(dest_path)
    makedirs(parent, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(full_html_page)




