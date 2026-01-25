import re
def extract_markdown_images(text):
    list_of_images = []

    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    return matches