from textnode import*
from shutil import*
from os import listdir
from os import mkdir
from os import path

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
    copy_tree("static", "public")
main()
