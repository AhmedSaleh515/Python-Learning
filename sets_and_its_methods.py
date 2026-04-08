# set
#----------
# enclosed in in curly braces
# not orderd and not indexed
mySetone = {"osama","Ahmed",'omar'}
print(mySetone) 
# print(mySetone[0]) this will through error cos its not indexed
# so set indexing and slicing cant be done cos slicing based on the indexing
 
 #set Has only immutable data typs (nums, strings, tuples) list and dict are not 

myset3 = {1.5, "a", 5, (1,2)}
print(myset3)
#myset4 = {1.5, "a", 5, [1,2]}
#print(myset3) error cos its accept only immutable data

# set items are unique
myset5 = {1,2,"ahmed","one","ahmed",1}
print(myset5) #it will print only {'ahmed', 1, 2, 'one'}
#########################################################
#########################################################
#______-------------sets method----------------________#
# clear()

a = {1,2,3}
a.clear()
print(a)

#union()
b = {"one", "two", "three"}
c = {"1","2","3"}
x = {"zero", "cool"}
print(b | c)
print(c | b)
print(b.union(c))
print(c.union(b,x))

# add()
d = {1,2,3,4}
#d.add(5,6) # cannot recevie more than one argument
d.add(5)
d.add(6)
print(d) #now its works fine

#copy()
e = d.copy()
print (d)
print (e)

# remove
e.remove(1)
#e.reomve(7) # error cos you have to chose exist element

#discard

d.discard(1)
d.discard(7) # now there is no error if you chose non exist element

# pop() pop here take random element from the set cos as we said you can not indexing in sets

# update()
j = {1,2,3}
k = {1,"A", "B", 2}
j.update(["html","css"])# you can update it with list
j.update(k) 
print(j) # same as union

#difference()
a = {1, 2, 3, 4}
b = {1, 2, "Ahemd", "Saleh"}
print(a)
print(a.difference(b)) # a - b
print(a)
print("="*20)
#difference _update()

c = {1, 2, 3, 4}
d = {1, 2, "Ahemd", "Saleh"}
print(c)
c.difference_update(d) # a - b
print(c)
print("="*20)

# intersection() intersection_update() --- update do update to the variable in you cde
e = {1,2,3,4,"X"}
f = { 2, "Ahemd", "X"}
print(e)
print(e.intersection(f)) # e & f
print(e)
e.intersection_update(f)
print(e)
print("="*25)


# symmetric_difference() and update
i = {1,2,3,4,5,"X"}
j = {1, 2,4 , "Ahemd", "saleh"}
print(i)
print(i.symmetric_difference(j)) # i^j
print(i)
i.symmetric_difference_update(j)
print(i)
print("="*20)

# issuperset()
a = {1,2,3,4,5}
b = {1,2,3}
c = {1,2,3,4,5,"X"}

print(a.issuperset(b)) # check if the element of b exist in a \True
print(a.issuperset(c)) # Fulse
print("="*20)

#issubset()
d = {1,2,3,4}
e = {1,2,3}
print(d.issubset(e))# does d is a subset in e \ False
print(e.issubset(d))# does e is a subset in d \ True
print("="*30)

# isdisjoint()
g = {1,2,3,4}
h = {1,2,3}
i = {10, 11, 12}
print(g.isdisjoint(h)) # fulse they aren't disjoint
print(g.isdisjoint(i)) # True they are disjoint
