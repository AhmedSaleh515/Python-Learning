#it has no name (anonymous function)
#you can call it inline without dwfining it 
#you can use it in return data from anther function
#used for simple function and def handle tha large tasks
#lambda is one single expression not block of code
# lambda type is function

def say_hello(name): return f"Hello {name}"
print(say_hello("Ahmed"))

#lambda:-
hello = lambda name, age : f"Hello {name} your age is {age}"
print(hello("Hammada,",43))

#check the name
print(say_hello.__name__)
print(hello.__name__)
print(type(hello))