from cryptography.fernet import Fernet

Master_password = input("Enter Your Master Password: ")

def add():
    name = input("Name: ")
    username = input("Username: ")
    Pass = input("Password :")
    with open(r'C:\Users\1\Desktop\Python coding\Password Manager\passwords.txt', 'a') as f:
        f.write(name +"|" + username + "|" + Pass + "\n")

def view():
    with open(r'C:\Users\1\Desktop\Python coding\Password Manager\passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            namee, user, passw = data.split("|")
            print("Name:", namee, "|","Username:", user, "|", "Password:", passw )

while True:
    mode = input("Would You Like To ADD or VIEW The Data ? (add/view) to quit the app press q :").lower().strip()
    if mode == "q":
        print("See You Later!")
        quit()
    
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid Choice Try Again Please")
        continue