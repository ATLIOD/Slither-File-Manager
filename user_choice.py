import globals
import traversal
import operations
from termcolor import colored

def user_action():
    globals.decision = input(colored("\nEnter Action\n1:open folder\n2:create folder\n3:open file\n4:create file\n5:move file\n6:copy file\n7:rename file\n8:Go to new path\nq:exit\n\n", attrs=['bold']))
    if globals.decision == '1':
        directoryName = input("Enter directory name: ")
        traversal.open_dir(directoryName)
        traversal.list_dir(globals.current_path)
    if globals.decision == '2':
         newDirectory = input("Enter name for new folder: ")
         operations.create_dir(newDirectory)
         traversal.list_dir(globals.current_path)
    if globals.decision == '3':
        fileName = input("Enter file name: ")
        traversal.open_file(fileName)
    if globals.decision == '4':
         newFile = input("Enter name for new file: ")
         operations.create_file(newFile)
         traversal.list_dir(globals.current_path)
    if globals.decision == '5':
        fileName = input("Enter name of file to move: ")
        destination = input("Enter destination: ")
        operations.move_file(fileName, destination)
        traversal.list_dir(globals.current_path)
    if globals.decision == '6':
        fileName = input("Enter name of file to copy: ")
        destination = input("Enter destination: ")
        operations.copy_file(fileName, destination)
        traversal.list_dir(globals.current_path)
    if globals.decision == '7':
        fileName = input("Enter the current name of the file: ")
        destination = input("Enter the new name of the file: ")
        operations.rename_file(fileName, destination)
        traversal.list_dir(globals.current_path)
    if globals.decision == '8':
        pathName = input("Enter full path to new directory: ")
        operations.goto_path(pathName)
        traversal.list_dir(globals.current_path)
