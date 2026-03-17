correct_username = 'Hamada'
correct_password = '123456'
attempts = 3
# this while loop check on the ursername
while attempts > 0 :
    username = input("Enter Your User Name (You have 3 attempts): ")
    if username == correct_username:
        print("Valid Username")    
        break
    else:
        print("invalid Username Try again(You still Have)",str(attempts-1),"chances")
    attempts -=1
# this while loop check on the password and i did reassign the attempts to 3     
attempts = 3
while attempts > 0 :
    if username != correct_username:
        print("System Locked. Call Security!")
        break
    password = input("Enter Your Password (You have 3 attempts): ")
    if password == correct_password:
        print("Valid Password you are in")    
        break
    else:
        print("invalid Password Try again(You still Have)",str(attempts-1),"chances")
    attempts -=1 
if password != correct_password:
        print("System Locked. Call Security!")
#_____________________________________________________________#
# ____________________________________________________________#
# the next code is improved by AI based on my own to make it better and tell me how to improve mysilf
# to run it and see how its work delete the(""")at the beginning and the end and put them infront of 
# and after the previous code
"""correct_user = "Hamada"
correct_pass = "123456"
attempts = 3

while attempts > 0:
    user_input = input("Username: ")
    pass_input = input("Password: ")

    if user_input == correct_user and pass_input == correct_pass:
        print("✅ Access Granted! Welcome, Hamada.")
        break 
    else:
        attempts -= 1
        print(f"❌ Invalid credentials. Tries left: {attempts}")

if attempts == 0:
    print("⛔ System Locked. Call Security!")   """          