import os

def traverse_filesystem(root_dir):
 #   print(os.walk(root_dir))
    for path, dirnames, filenames in os.walk(root_dir):
        print('{} {} {}'.format(repr(path), repr(dirnames), repr(filenames)))

traverse_filesystem("/home/Dom")
