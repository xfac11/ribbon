from textnode import TextNode
from textnode import TextType

def supporting_delimiter(delimiter, text_type):
    if delimiter == "**" and text_type == TextType.BOLD:
        return True
    if delimiter == "_" and text_type == TextType.ITALIC:
        return True
    if delimiter == "`" and text_type == TextType.CODE:
        return True
    return False

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    if not supporting_delimiter(delimiter, text_type):
        raise ValueError(f"Not matching delimiter with text type. Delimiter: '{delimiter}' and text_type: '{text_type}'")
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue
        
        split_text = old_node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise SyntaxError(f"Invalid markdown syntax: No closing '{delimiter}' was found in '{old_node.text}'")
        for i in range(0, len(split_text)):
            if split_text[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(split_text[i], TextType.PLAIN))
            else:
                new_nodes.append(TextNode(split_text[i], text_type))
    return new_nodes