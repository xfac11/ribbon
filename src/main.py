from textnode import*
from shutil import*
from os import listdir
from os import mkdir
from os import path
import sys
from generatepage import generate_page
from generatepagesrecursive import generate_pages_recursive
def copy_tree_r(source, destination):
    if not path.exists(source):
        raise TypeError(f"Source path: {source} does not exist")
    if path.isfile(source):
        return
    dir = listdir(source)
    for file in dir:
        if not path.isfile(path.join(source,file)):
            mkdir(path.join(destination,file))
            copy_tree_r(path.join(source,file), path.join(destination, file))
        if path.isfile(path.join(source, file)):
            copy(path.join(source,file), destination)
    

def copy_tree(source, destination):
    rmtree(destination)
    mkdir(destination)
    copy_tree_r(source, destination)

def main():
    base_path = "/"
    if len(sys.argv) < 1:
        base_path = sys.argv[1]
    


    copy_tree("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", base_path)
main()
