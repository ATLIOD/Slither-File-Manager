import os
import subprocess
import globals

def list_dir(root_dir):
    subdirectories = []
    files = []
    for entry in os.scandir(root_dir):
        if entry.is_dir():
            subdirectories.append(entry)
        elif entry.is_file():
            files.append(entry)
    print("subdirectories:")
    for each in subdirectories:
        print(each.name)
    print("files:")
    for each in files:
        print(each.name)

'''
    for dirpath, dirnames, filenames in os.walk(root_dir):
        print(
            f"Root: {dirpath}\n"
            #f"sub-directories: {dirnames}\n"
            #f"Files: {filenames}\n\n"
            )
'''
def open_dir(selectionName):
    for entry in os.scandir(globals.current_path):
        if entry.is_dir() and entry.name == selectionName:
            selection = entry
            list_dir(selection.path)
            globals.current_path = selection.path
            return 0
        else:
            pass

def open_file(selectionName):
    if selectionName not in os.listdir(globals.current_path):
        print("File not found")
    else: 
        subprocess.call("xdg-open " +
                        os.path.join(globals.current_path,selectionName), shell
                        = True)
