# Decorator intro 
# 1 Somtimes called meta programming
# 2 Everything in python is object even function 
# 3 Decorator take a function and add some functionality and return it
# 4 Decorator wrap other fuunction and enhance their behaviour
# 5 Decorator is higher order function (Function accept function as parameter)

def myDecorator (func) : # decorator
    def nestedFunc() : # Anyname its just for decoration
        print ("Before")

        func() # Execute functon

        print("After")
    return nestedFunc

@ myDecorator
def sayHello():
    print("Hello form Hello function Hamada")


sayHello()

# This is how to make it
print("**"*25)
# Now we will try it with parameter Real use of decorator
def my2Decorator (func):
    def checknumber(num1, num2):
        if num1<0 or num2<0:
            print ("Beware One of the numbers is less than zero")
        func(num1, num2)
    return checknumber
@ my2Decorator
def calculate(n1, n2):
    print(n1 + n2)

calculate(10, 90)
#the second meets the condition so you will see the message
#and it will run anyway don't wory :)
calculate(-10,10)

print("**"*25)
#you can also run two decorators on one function