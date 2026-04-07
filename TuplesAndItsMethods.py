#Tuples Enclosed in parentheses
my_first_tuple = ("Ahmed","Saleh")

#you can remove the parentheses if you want
my_Second_tuple = "Ahmed","Saleh","Mohammed"

print(my_first_tuple)
print(my_Second_tuple)

print(type(my_first_tuple))
print(type(my_Second_tuple))

#tuple are ordered, to use index to access item
#tuple indexing
my_third_tuple = (1,2,3,4,5,6)
print(my_third_tuple[0])
print(my_third_tuple[4])
print(my_third_tuple[-1])

#tuple are immutable 
#you cannot assign new values
#my_third_tuple[2] = "three" error
#cannot assign or do anything else affect the values 

#tuples are not unique 
tuple_five = 1,2,2,3,5,1,5,2
print(tuple_five)

#tuples can accept any data type
tuple_6 = "os", 1,1.45,True
print(tuple_6)

# to declare tuple with one element you have to write it like this
tuple_7 = ("Ahmed",) # should add comma <,>

#tuple, list, string repeat (*)
myString = "Ahmed"
myList = [1, 2]
myTuple = ('a','b')
print(myList*5)
print(myString*5)
print(myTuple*5)

# count() method also works here 
print(tuple_five.count(2))

# tuple destruct
a = ("a", "b" , "c")
x, y ,z = a
print(x, y, z)

a = ("a", "b",5 , "c")
x, y,_ ,z = a # <_> the underscore ignores the selected element
print(x, y, z)