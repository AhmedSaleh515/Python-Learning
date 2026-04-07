#------------------------#
#------Lists Methods-----#

#append() to add to list

myFrinds = ["Malaz", "Simon", "Anas"]
myOldFriends = ["Abdullah","Mohammed"]
print(myFrinds)
myFrinds.append("Emad") 
myFrinds.append(102) 
myFrinds.append(15.256) 
myFrinds.append(True) 
print(myFrinds)

# you can add any type of data but if you added list it will be added as one element

myFrinds.append(myOldFriends)
print(myFrinds)
print(myFrinds[2])
print(myFrinds[6])
print(myFrinds[7])# its added as on element
print(myFrinds[7][1]) # you can access its elements

#extend() this method add list to list in one list
a = [1,2,3]
b = ['a','b','c']
c = ['one', 'two']
a.extend(b)
print(a)
a.extend(c)
print(a)

# remove() to remove elements from list
x = [1,2,3,4,5, "Ahmed", True, "Ahmed", "Ahmed"]
x.remove("Ahmed")
print(x) # its remove only the first element corrosponding

# sort() to sort form small to large
y = [1, 2, 100, 120, -10, 17, 29]
y.sort() # there is an option called (reverse) and its bydefult  = false
print(y)
y.sort(reverse=True)
print(y) # sort can also work with strings but you can not mix it with int in one list 

# reverse() reverse the list without sorting

z = [10, 1, 9, 80, 100, "Ahmed", 100]
z.reverse()
print(z)

# clear() removes all items from the list
a = [1, 2, 3]
a.clear()
print(a)

# copy()
b = [1, 2, 3, 4]
c = b.copy()
print(b) # main list
print(c) # copied lsit
b.append(5)
print(b)
print(c)

# count()
d = [12,3,3,5,4,85,2,2,4,3]
print(d.count(3))
print(d.count(12))
print(d.count(33))

#index() find the index of an element
e = ["Malaz", "Simon", "Anas"]
print(e.index("Malaz"))
#print(e.index("mosa")) you can not index what is not exist

# insert () unlike append(), insert() let you spicify where you want to add you new element
e = ["Malaz", "Simon", "Anas"]
e.insert(0, "Test")  # insert elements before the place you give it
print(e)
e.insert(-1,"Tet")
print(e)

# pop()

g =  [1, 2, 3, 4]
print(g.pop(2))
print(g)