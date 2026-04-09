#-----------------------#
# built in functions 
#-----------------------#

# all()  all function 
from functools import reduce


x =[1,2,3,4]

if all(x): # if all element in the list is true
    print ("all elements is true")
else:
    print("there is at lease one element is False")

print("111"*20)

x =[1,2,3,4,[]]

if any(x): # if any element in the list is true 
    print ("there is at lease one element is True")
else:
    print("non of the elemnt is true")
print("222"*20)

print(bin(100)) # bin converts to binary

a = 1 
b = 2
print(id(a), id(b))# the address in the memory 

print("333"*20)

# sum(iterable, start)

n = [1,2,3,4,5,6,7,8,9]
print(sum(n))
print("444"*20)

#round(number, number of digits)
print(round(150.452))
print(round(150.650))
print(round(150.556,2))
print("5"*50)
# range(start, end, step) you have always to give it end but the start and the step it has defualt number
print(list(range(10)))
print(list(range(0,20,2)))
print("666"*20)

#print()
print("Hello Osama")
print("Hello","Osama")
print("Hello","Osame",sep = "|")
print("First line") # the end by defualt = \n
print("second line") #but u can change it to what you need using end=
print("first line", end = "Look i am the end ")
print("second line", end="\n")
print("third line")
print("777"*20)
#abs() abslute value
print(abs(100))
print(abs(-100))
print(abs(10.19))
print(abs(-10.19))
print("8"*50)

# pow(base,exp, mod) power
print(pow(2, 5)) #2x2x2x2x2 or2^5
print(pow(2,5,10)) #2^5%10
print("999"*20)

#min(item, item, item...  or  iterator) the minimum value
print(min(1,10,-50,20)) #items
print(min("a","b","ahmed"))#items
myNums = (1,10,20,-5,24)
print(min(myNums))# iterator
print("10-"*20)

#max(item, item, item...  or  iterator) the maximum value
print(max(1,10,-50,20)) #items
print(max("a","b","ahmed"))#items
myNums = (1,10,20,-5,24)
print(max(myNums))# iterator
print("11-"*20)

# slice()
a = ['A','B','C','D']
print(a[:2])
print(a[slice(2)])
print(a[slice(1,2)])
print("12-"*20)

#-----------------------#
# Map 
#  1- Map take a function + Iterator
#  2- Map called map because it map the function on every element
#  3- The function can be pre-defined function or lambda function

def formatText(name):
    return f"- {name} -"

myNames = ["Ahmed", "Saleh", "Mohammed"]

myFormatedData = map(formatText, myNames)

#print (myFormatedData)

for name in myFormatedData:
    print(name)

for name in map(formatText, myNames):
    print(name)
for name in list(map(formatText, myNames)):
    print(name)    

# Use map with lembda function
myNames = ["Ahmed", "Saleh", "Mohammed"]
for name in list(map(lambda name : f"- {name} -",myNames)):
    print(name)

print("13-"*20)

#-----------------------#
# Filter
# 1- Filter take a function + iterator
# 2- Filter run a function on every element 
# 3- The function can be pre-defined or Lambda function
# 4- Filter out all elements for which the function return true
# 5- The function need to return boolean value

def checkNumber(num):
        return num > 10
myNumbers = [1,19,10,20,100,5]
myResult = filter(checkNumber, myNumbers)
for number in myResult:
    print(number)
print("14-"*20)

def checkname(name):
        return name.startswith("A")
myNames = ["Ahmed", "Amani","Saleh","Mohameed"]
myResult = filter(checkname, myNames)
for name in myResult:
    print(name)
print("14-"*20)

# try the same with lambda function
myNames = [ "Amani","Saleh","Mohameed","Awadh"]
myResult = filter(lambda name : name.startswith("A"), myNames )
for name in myResult:
    print(name)
print("14-"*20)

#-----------------------#
# Reduce Function
# 1- Reduce take a function + iterator 
# 2- Reduce run a function on first and second Element and give result
# 3- Then run function on result and third element 
# 4- Then run function on result and fourth element and so on
# 5- Till one element is left and this is the result of the reduce
# 6- The function can be Pre-defined of lambda function 
def sumAll(num1, num2):
     return num1 + num2
numbers = [1,8,2,9,100]
reslut = reduce(sumAll,numbers) #  ((((1+8)+2)+9)+100)
print(reslut)

print("15-"*20)
#using lambda:
resluty = reduce(lambda num1, num2 : num1+num2 ,numbers)
print(resluty)
print("15-"*20)

# enumerate(iterable, start=0 optional) function

mySkills = ["Html", "Css", "JS", "PHP"]

mySkillsWithCounter = enumerate(mySkills , 1) 
# ,1 is the number u want the counter start from u can chose any number and its 0 by defualt
for skill in mySkillsWithCounter:
     print(skill)

print("16-"*20) 
mySkillsWithCounter = enumerate(mySkills , 1) 
for counter, skill in mySkillsWithCounter:
     print(f"{counter} - {skill}")

print("16-"*20) 

# help() helps you if you don't kknow about function for example here the function print

print(help(print))
print("17-"*20) 

# reversed(iterable) reversed any iterable 
mystring = "AlHebshi"
print(reversed(mystring))
print("18-"*20) 

for letter in reversed(mystring):
     print(letter)
print("18-"*20) 

mySkills = ["Html", "Css", "JS", "PHP"]
for s in reversed(mySkills):
     print(s)

print("18-"*20)
