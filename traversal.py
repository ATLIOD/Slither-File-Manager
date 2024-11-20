import os
import subprocess
import globals
from termcolor import colored

def list_dir(root_dir):
    subdirectories = []
    files = []
    for entry in os.scandir(root_dir):
        if entry.is_dir():
            subdirectories.append(entry)
        elif entry.is_file():
            files.append(entry)
    subprocess.call("clear")
    print(colored(globals.current_path,"magenta",attrs = ["bold", "underline"]))
    print(colored("subdirectories:", "red"))
    for each in subdirectories:
        print(colored(each.name, "light_red"))
    print(colored("files:", "cyan"))
    for each in files:
        print(colored(each.name, "light_cyan"))

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
            globals.current_path = selection.path
        else:
            pass

def open_file(selectionName):
    if selectionName not in os.listdir(globals.current_path):
        print("File not found")
    else: 
        subprocess.call("xdg-open " +
                        os.path.join(globals.current_path,selectionName), shell
                        = True)
