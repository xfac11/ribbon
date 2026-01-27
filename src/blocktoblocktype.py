from blocktype import BlockType
def is_heading(block):
    index = 0
    while block[index] == "#":
        index += 1
        if index > 6:
            break
    if index == 0 or index > 6:
        return False
    if block[index] == " " and block[index+1] != "":
        return True
    return False

def is_code(block):
    if block[0] != "`" or block[1] != "`" or block[2] != "`" or block[3] != "\n" or block[-1] != "`" or block[-2] != "`" or block[-3] != "`":
        return False
    return True

def is_quote(block):
    split = block.split("\n")
    for line in split:
        if line[0] == ">":
            continue
        return False
    return True

def is_unordered_list(block):
    split = block.split("\n")
    for line in split:
        if line[0] == "-" and line[1] == " ":
            continue
        return False
    return True

def is_ordered_list(block):
    split = block.split("\n")
    number = 1
    for line in split:
        if line[0] == str(number) and line[1] == "." and line[2] == " ":
            number += 1
            continue
        return False
    return True

def block_to_block_type(block):
    if is_heading(block):
        return BlockType.HEADING
    if is_code(block):
        return BlockType.CODE
    if is_quote(block):
        return BlockType.QUOTE
    if is_unordered_list(block):
        return BlockType.UNORDERED_LIST
    if is_ordered_list(block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH