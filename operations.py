import os
import globals
import subprocess

#create a directory
def create_dir(name):
    if name not in os.listdir(globals.current_path):
        os.mkdir(os.path.join(globals.current_path,name))
# create a file
def create_file(name):
    print("making file")
    open(os.path.join(globals.current_path,name), "x")
#move a file
def move_file(name,destination):
    if name not in os.listdir(globals.current_path):
        print("File not found")
    else:
        subprocess.call("mv " +
                        os.path.join(globals.current_path,name) + " " + destination, shell
                        = True)
#copy a file to a destination
def copy_file(name,destination):
    if name not in os.listdir(globals.current_path):
        print("File not found")
    else:
        subprocess.call("mv " +
                        os.path.join(globals.current_path,name) + " " + destination, shell
                        = True)
#rename a file
def rename_file(name,newName):
    if name not in os.listdir(globals.current_path):
        print("File not found")
    else:
        subprocess.call("mv " +
                        os.path.join(globals.current_path,name) + " " + os.path.join(globals.current_path,newName), shell
                        = True)

# enter a full path to travel to
def goto_path(pathTo):
        if os.path.exists(pathTo):
            globals.current_path = pathTo
        else:
            print("Path does not exist")
