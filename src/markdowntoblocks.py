def markdown_to_blocks(markdown):
    blocks = []
    split_double_newlines = markdown.split("\n\n")
    for block in split_double_newlines:
        if block == "" or block == "\n":
            continue
        blocks.append(block.strip())
    return blocks