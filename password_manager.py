pwd = input("What is the master password? ")

def view():
    pass

def add():
    pass




while True:
    mode = input("Would you like to add a new password or view an existing one (view, add), or q to quit ").casefold()

    if mode == "q":
        break

    if mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid mode")
        continue