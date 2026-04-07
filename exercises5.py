#dictionary basics exercise(simple lookup system)
contacts = {'ahmed': 13157698216, 
        'malaz': 13157699182,
         'hamada': 158965468 }
name = str(input("enter an name to check: ").strip().lower())
if name in contacts:
    print(f"{name} is exist and its number is {contacts[name]} ")
else :
    print("the name is not found")
#this is a simpler way to do so
number = contacts.get(name, "Number not found")
print(f"{name}: {number}")
#__________________________________________________________________#
#__________________________________________________________________#
#__________________________________________________________________#
# guest list fulter (sets)
raw_guests = ["Ahmed", "Sara", "Ahmed", "John", "Sara", "Mona"]
unique_guests  = set(raw_guests)
unique_guests.add("Ali")
unique_guests.add("Sara")
print(unique_guests)
print(len(unique_guests))
#__________________________________________________________________#
#__________________________________________________________________#
#__________________________________________________________________#
# login system (nested dictionaries)
database = {"Hamada": {"pw": "secure123", "role": "Full Access"}, "Loza": {"pw": "pass1", "role": "Read Only"}}
username = input("Enter your username: ")
if username in database:
    chance = 3
    while chance > 0:
        password = input("Enter your password: ")
        if password == database[username]['pw']:
            print(f"Wlcome back {username} your role is: {database[username]['role']}")
            break
        else: 
            print("Sorry Wrong password try again please")
            chance -= 1
else:
    print("Sorry User not found")            

