from cryptography.fernet import Fernet

Master_password = input("Enter Your Master Password: ")

# function doing the add mode
def add():
    name = input("Name: ")
    username = input("Username: ")
    Pass = input("Password :")
    with open(r'C:\Users\1\Desktop\Python coding\Password Manager\passwords.txt', 'a') as f:
        f.write(name +"|" + username + "|" + Pass + "\n")


#function doing the view mode and its using yield instead of return which called generator
def view_generator():
    try:
        with open(r'C:\Users\1\Desktop\Python coding\Password Manager\passwords.txt', 'r') as f:
            for line in f:
                data = line.rstrip()
                if "|" in data:
                    yield data.split("|") # هنا "نُنتج" حساباً واحداً وننتظر
    except FileNotFoundError:
        print("No passwords found yet.")

# start the app::

while True:
    mode = input("Would You Like To ADD or VIEW The Data ? (add/view) to quit the app press q :").lower().strip()

    # quit mode
    if mode == "q":
        print("See You Later!")
        quit()

    # add mode using the function above
    if mode == "add":
        add()

    # view mode using the generator above
    elif mode == "view":
        print("\n------------ Your Stored Passwords ------------")
       
        for entry in view_generator():
            name, user, psw = entry
            print(f"Name: {name} | User: {user} | Pass: {psw}")
        print("------------------------------------------------\n")
    else:
        print("Invalid Choice Try Again Please")
        continue