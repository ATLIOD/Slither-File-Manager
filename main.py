import traversal, globals, user_choice

def main():
    traversal.list_dir(globals.USER_PATH)
    while globals.decision != 'q':
       user_choice.user_action()




if __name__ == '__main__':
    main()
