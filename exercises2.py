# this code is a practice for slicing i should rearrange a word to make it encrypted 
# by move the first 2 letters to the end and then write the word backward 
wordToEncrypt = input('Enter a word you want to encrypt: ') #python
EncryptedWord = wordToEncrypt[2:] #thon
EncryptedWord = EncryptedWord +wordToEncrypt[0:2] #thonpy
EncryptedWord = EncryptedWord[::-1] #ypnoht
print(EncryptedWord)

# this line is short cut for what i did made by AI
# encrypted = (wordToEncrypt[2:] + wordToEncrypt[:2])[::-1] 

# the next exercise is for if and while and function i am building a converter tool 

def convert_temperature(celsius):
    fehrenhait = (celsius*9/5) +32
    print(celsius,"celsius is",fehrenhait,"in fehrenhait")
def convert_distance(km):
    miles = km * 0.621371
    print(distance,"KM is",miles,"in miles")
choose = 1
while choose==1:
    print('Welcome to Unit Converter\n')
    print('1. Temperature\n2. Distance\n3. Exit')
    choose = int(input('Please enter the number of your choice: '))
    if choose == 1 :
        temp = int(input("Enter the celsius degree you want to convert:"))
        convert_temperature(temp)
        print("Thank You for using our tool")
        break

    elif choose == 2 :
        distance = int(input("Enter the KM Distance you want to convert:"))
        convert_distance(distance)
        print("Thank You for using our tool")

    else:
        print("See You Later")    

## the comming code is made by AI its easier and better version for my own code doing the same thing
# 
""" 
# 1. Functions that focus ONLY on the math (Input/Output)
def convert_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_to_miles(km):
    return km * 0.621371

# 2. The main program loop
while True:
    print("\n--- Unit Converter Menu ---")
    print("1. Celsius to Fahrenheit")
    print("2. Kilometers to Miles")
    print("3. Exit")
    
    choice = input("Select an option (1-3): ")

    if choice == '1':
        c = float(input("Enter Celsius: "))
        f = convert_to_fahrenheit(c)
        print(f"Result: {c}°C is {f}°F")

    elif choice == '2':
        k = float(input("Enter Kilometers: "))
        m = convert_to_miles(k)
        print(f"Result: {k} km is {round(m, 2)} miles")

    elif choice == '3':
        print("Goodbye!")
        break  # This kills the loop and ends the program

    else:
        print("Invalid choice, please try again.")
"""