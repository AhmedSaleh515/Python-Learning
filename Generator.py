#__________________________#
#-------Generators---------#
#__________________________#
# 1 Generator is a function with -yield- keyword instead of -return-
# 2 It support iteration and return generator iterator by calling yield
# 3 generator function can have one or more "yield"
# 4 by using next() it resume from where it called "yield" not from begining
# 5 when called, its not start automatically, its only give you the control 
#____________________________________________________________________________#

def myGenerator():
    yield 1
    yield 2
    yield 3
    yield 4
myGen = myGenerator()
print(next(myGen))

print ("hello from python ")
print(next(myGen))
print(next(myGen))

print("generator always start from where the last point")
print(next(myGen))
# print(next(myGen)) stop iteration error cos its more than four as in the generator

print ("()"*25)

# You can also loop throgh the genrator

def my2Generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
my2gen = my2Generator()
for number in my2gen:
    print (number)

