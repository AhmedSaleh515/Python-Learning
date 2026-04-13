import random  
# roll the dice
"""while True:
   
    choise = input("Do you wanna roll the Dice? (y/n): ").lower().strip()
    
    if choise == "y":
      
        print(f"[{random.randint(1, 6)} | {random.randint(1, 6)}]")
    elif choise == "n":
        
        print("Goodbye!")
        break
    else:
        print("Invalid input, please type 'y' or 'n'.") """

#guess the number

"""num_to_guess = random.randint(1, 100)
while True:
    user_num = input("Guess the Number between 1 and 100 :")
    if user_num.isdigit():
        user_num = int(user_num)
        if user_num > num_to_guess:
            print("you are to high!")
        elif user_num < num_to_guess:
            print("you are to low!")
        else: 
            print(f"you did it the number is {num_to_guess}")
            break
    else:
        print ("please inter a number") """

# rock paper and scissors
options = ["r" , "p", "s"]
while True:
    computer_Choise = str(random.choice(options))
    user_choise = input("Rock, Paper, Scissors (r,p,s)(Enter  q to qiut):").strip().lower()
    if user_choise == "q":
        print("Thank you to play with us")
        break
    if user_choise not in options:
        print("invalid choice")
        continue
        # Rock Choice
    if user_choise == 'r' and computer_Choise == 's':
        print ("Your choice is Rock | Computer Choice is Scissors")
        print ("---------------------You Won!!-------------------")
    elif user_choise == 'r'and computer_Choise == "p":
        print ("Your choice is Rock | Computer Choice is Paper")
        print ("-----------------You Lose!!-------------------")
    elif user_choise == 'r'and computer_Choise == "r":
        print ("Your choice is Rock | Computer Choice is Rock")
        print ("-------------------Draw!!--------------------")
        #Paper Choice
    elif user_choise == 'p' and computer_Choise == 's':
        print ("Your choice is Paper | Computer Choice is Scissors")
        print ("---------------------You Lose!!-------------------")
    elif user_choise == 'p'and computer_Choise == "p":
        print ("Your choice is Paper | Computer Choice is Paper")
        print ("--------------------Draw!!---------------------")
    elif user_choise == 'p'and computer_Choise == "r":
        print ("Your choice is Paper | Computer Choice is Rock")
        print ("------------------You Won!!-------------------")
    #Scissors Choice
    elif user_choise == 's' and computer_Choise == 's':
        print ("Your choice is Scissors | Computer Choice is Scissors")
        print ("------------------------Draw!!-----------------------")
    elif user_choise == 's'and computer_Choise == "p":
        print ("Your choice is Scissors | Computer Choice is Paper")
        print ("--------------------You Won!!---------------------")
    elif user_choise == 's'and computer_Choise == "r":
        print ("Your choice is Scissors | Computer Choice is Rock")
        print ("-------------------You Lose!!--------------------")
