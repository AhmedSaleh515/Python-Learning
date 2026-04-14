def sayHello(nme):
    print(f"Helllo {nme}")

def sayHowAreYou (name) :
    print (f"How are you {name}")

import modules  # import the module
modules.sayHello("Hamada")

from modules import sayHowAreYou #import only one function from the module
sayHowAreYou("Hamada")
#it will print twice cos we are in same file 
#and there is no need to call module in the same file you did generate it this one only for explaining

import pyfiglet
print(pyfiglet.figlet_format("Hamada"))
import termcolor
print (termcolor.colored("Hamada", color="yellow"))
print (termcolor.colored(pyfiglet.figlet_format("HAMADA515"),color="red"))