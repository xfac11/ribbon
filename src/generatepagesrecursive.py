import os
from generatepage import generate_page
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.isfile(dir_path_content) and dir_path_content.endswith('.md'):
        generate_page(dir_path_content, template_path, dest_dir_path.replace(".md", ".html"))
        return
    files = os.listdir(dir_path_content)
    for file in files:
        generate_pages_recursive(os.path.join(dir_path_content, file), template_path,  os.path.join(dest_dir_path, file))