import os
import globals

def create_dir(name):
    if name not in os.listdir(globals.current_path):
        os.mkdir(os.path.join(globals.current_path,name))
def create_file(name):
    print("making file")
    open(os.path.join(globals.current_path,name), "x")
