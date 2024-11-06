import globals
import traversal
import operations

def user_action():
    globals.decision = input("Enter Action\n1:open folder\n2: create folder\n3:open file\n4:create file\n5: print current path\n6: print current directory contents\nq:exit\n\n")
    if globals.decision == '1':
        directoryName = input("Enter directory name:")
        traversal.open_dir(directoryName)
    if globals.decision == '2':
         newDirectory = input("Enter name for new folder:")
         operations.create_dir(newDirectory)
    if globals.decision == '3':
        fileName = input("Enter file name:")
        traversal.open_file(fileName)
    if globals.decision == '4':
         newFile = input("Enter name for new file:")
         operations.create_file(newFile)
    if globals.decision == '5':
        print(globals.current_path)
    if globals.decision == '6':
        print(traversal.list_dir(globals.current_path))
