from extractmarkdownimages import extract_markdown_images
from textnode import TextNode
from textnode import TextType

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue
        
        text_url_pair_list = extract_markdown_images(old_node.text)
        
        text_to_split = old_node.text
        for text_url in text_url_pair_list:
            alt_text = text_url[0]
            url = text_url[1]
            split_text_and_image = text_to_split.split(f"![{alt_text}]({url})", maxsplit=1)

            if split_text_and_image[0] != "":
                new_nodes.append(TextNode(split_text_and_image[0], TextType.PLAIN))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            
            text_to_split = split_text_and_image[1]
        
        if text_to_split != "":
            new_nodes.append(TextNode(text_to_split, TextType.PLAIN))


    return new_nodes