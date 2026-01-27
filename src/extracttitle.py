def extract_title(markdown):
    if markdown[0] == "#" and markdown[1] == " ":
        split_title_rest = markdown.split("\n", maxsplit = 1)
        title = split_title_rest[0]
        title = title[2:]
        title = title.strip()
        return title
    raise Exception("No header found in the markdown file. Please put one at the top of the file")


