name = "HAMADA" 
print(name[1])
print(name[0])
print(name[5])
#print(name[6])  out of range

#if i want the last char but i don't know how long is the string is 
#then i should use '-' negative sign
#its let me move backward
print(name[-1])
print(name[-2])

message = "A kong string with silly typo"
#message[2] = 'l'   we cannot change individual char cos string in python are immutable 
#to solve it 
new_message = message[0:2] + 'l' + message[3:]
print(new_message)

#but we can assign a new value 
message = "This is a new message"
print(message)

#how we are suppose to know which char to change??

Pets = "Cats & Dogs"
print(Pets.index("&") ) # now we know where is this char

# to check if a substring is contained in string we use "in"
print("Dragons" in Pets)
print("Cats" in Pets) 

