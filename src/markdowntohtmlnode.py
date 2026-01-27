from htmlnode import*
from textnode import*
from blocktoblocktype import*
from markdowntoblocks import markdown_to_blocks
from parentnode import ParentNode
from leafnode import LeafNode
from texttotextnodes import text_to_textnodes
from textnodetohtmlnode import text_node_to_html_node
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children

def create_quote_html_node(block):
    children = text_to_children(block[2:])
    parent_node = ParentNode("blockquote", children)
    return parent_node

def create_ordered_list_html_node(block):
    list_items = block.split("\n")
    children = []
    for list_item in list_items:
        children.append(ParentNode("li", text_to_children(list_item[3:])))
    parent_node = ParentNode("ol", children)
    return parent_node

def create_unordered_list_html_node(block):

    list_items = block.split("\n")
    children = []
    for list_item in list_items:
        children.append(ParentNode("li", text_to_children(list_item[2:])))
    parent_node = ParentNode("ul", children)
    return parent_node

def create_heading_html_node(block):
    index = 0
    while block[index] == "#":
        index += 1
    children = text_to_children(block[index+1:])
    
    parent_node = ParentNode(f"h{index}", children)
    return parent_node

def create_paragraph_html_node(block):
    block = block.replace("\n", " ")
    children = text_to_children(block)
    parent_node = ParentNode("p", children)
    return parent_node

def create_code_html_node(block):
    code_text = block[4:-3]
    parent_node = ParentNode("pre", [ParentNode("code", [text_node_to_html_node(TextNode(code_text, TextType.PLAIN))])])
    return parent_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                block_nodes.append(create_paragraph_html_node(block))
            case BlockType.CODE:
                block_nodes.append(create_code_html_node(block))
            case BlockType.HEADING:
                block_nodes.append(create_heading_html_node(block))
            case BlockType.UNORDERED_LIST:
                block_nodes.append(create_unordered_list_html_node(block))
            case BlockType.ORDERED_LIST:
                block_nodes.append(create_ordered_list_html_node(block))
            case BlockType.QUOTE:
                block_nodes.append(create_quote_html_node(block))
        
    parent_node = ParentNode("div", block_nodes)
    return parent_node