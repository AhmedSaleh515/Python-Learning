# List contains admins
admins = ["Ahmed", "Hamid", "Malaz","Mohammed"]
# Login
name = input("Please Enter your Name: ").strip().capitalize()

# if name is in admin
if name in admins:
    print(f"Hello {name} welcome back")
    while True:
        option = input("Delete of Update your name?").strip().lower()
        if option == "update":
            the_new_name = input("Entere your new name please: ").strip().capitalize()
            admins[admins.index(name)] = the_new_name
            print ("Your Name Updated")
            print(admins )
            break
        elif option == "delete"  :
            admins.remove(name) 
            print("your name is Deleted")
            print(admins)
            break
        else:
            print(f"the feture {option} is not availabe try again please with (update\\delete)")

else:
    password = 1234
    chance = 3
    status = input("You are not admin. Do you want to regester as a new admin? (yes\\no):").strip().lower()
    while chance > 0:
        if status == "yes":
            user_pass = int(input("Enter the regester Password: "))
            
            if user_pass == password:
                new_user = input("Enter your username want to regeter with: ").capitalize().strip()
                admins.append(new_user)
                print("Congratlation You are new admin")
                print(admins)
                break
            else:
                chance-=1
                print(f"wrong Password, you still have {chance} chances.")
        else:
            print("Thank you for using our system")