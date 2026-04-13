print("Welcome To My Quiz!")
score = 0

playing = input("Wanna Play (y/n) ? ").lower().strip()
if playing != "y":
    quit()

#Q1
answer = input("What does CPU stand for? \n").lower().strip()
if answer == "central processing unit":
    print("Correct Answer :)")
    score += 1
else:
    print("Wrong Answer :(")

#Q2
answer = input("What does GPU stand for? \n").lower().strip()
if answer == "graphics processing unit":
    print("Correct Answer :)")
    score += 1
else:
    print("Wrong Answer :(")

#Q3
answer = input("What does RAM stand for? \n").lower().strip()
if answer == "random access memory":
    print("Correct Answer :)")
    score += 1
else:
    print("Wrong Answer :(")
#Q4
answer = input("What does PSU stand for? \n").lower().strip()
if answer == "power supply":
    print("Correct Answer :)")
    score += 1
else:
    print("Wrong Answer :(")

#Q5
answer = input("What is the main circuit board of a computer called? \n").lower().strip()
if answer == "motherboard":
    print("Correct Answer :)")
    score += 1
else:
    print("Wrong Answer :(")
#Q6
answer = input("What does HTTP stand for in a website address? \n").lower().strip()
if answer == "hypertext transfer protocol":
    print("Correct Answer :)")
    score += 1
else:
    print("Wrong Answer :(")

#Q7
answer = input("What does GUI stand for in reference to a visual operating system? \n").lower().strip()
if answer == "graphical user interface":
    print("Correct Answer :)")
    score += 1
else:
    print("Wrong Answer :(")

#Q8
answer = input("What does BIOS stand for? \n").lower().strip()
if answer == "basic input output system":
    print("Correct Answer :)")
    score += 1
else:
    print("Wrong Answer :(")

#Q9
answer = input("What does DNS stand for? \n").lower().strip()
if answer == "domain name system":
    print("Correct Answer :)")
    score += 1
else:
    print("Wrong Answer :(")

#Q10
answer = input("What does SSD stand for in modern storage drives? \n").lower().strip()
if answer == "solid state drive":
    print("Correct Answer :)")
    score += 1
else:
    print("Wrong Answer :(")
print(f"you got {score} answers correct")
print(f"Your Score is {score /10 * 100} % ")




