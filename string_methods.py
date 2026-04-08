#-------------------------#
#-----String's Methods------#

# strip() rstrip() lstrip() remove the spaces at the end and the beginning
# and if you give it a spicific char it will remove it also
a = '   I love Python      '
print(a)
print(a.strip())
print(a.lstrip())
print(a.rstrip())

a = '####I love Python####'
print(a)
print(a.strip('#'))
print(a.lstrip('#'))
print(a.rstrip('#'))
a = 'love love love'
print(a.strip('love'))

# title() convert the first letter in each work in the string to uppercase
b = 'I Love 2d Graphics and 3g Technology and python'
print(b.title())

# capitalize() conver only the furst letter in the string to uppercase
b = 'i Love 2d Graphics and 3g Technology and python'
print(b.capitalize())

#zfill fill zero based of what you asked it to fill 

c, d, e = '1', '11' , '111'
print(c)
print(d)
print(e)

print(c.zfill(3)) # if it 4 it will write three zeros
print(d.zfill(3))
print(e.zfill(3))

# upper()  lower() convert the whole string to upper of lowercase
g = "ahmed"
print(g.upper())
g = 'AHMeD'
print(g.lower())

#split() rsplit() convert the string to list

e = "i love python and php"
print(e.split()) 

e = "i-love-python-and-php"
print(e.split()) #by defult it will splited based on the spaces
print(e.split('-')) # now i told the method to split based on the -
print(e.split('-', 2)) # max split told the method to split only two times then put the rest in one item
print(e.rsplit('-', 2)) # r split do the same as max split but from the right side

# center() 
e = "Ahmed"
#print(e.center()) you can not give zero argument to .center()
print(e.center(9)) #spaces 9 in total and the reset 2 in the right and 2 in the left
print(e.center(9,'#')) #Hashes
print(e.center(15,'@')) #Hashes

# count() it counts what you give it as argument
f = "I Love Python and PHP Because PHP is Easy"
print(f.count("PHP")) 
print(f.count('is'))
print(f.count('PHP', 0, 25))# now i did give it range to search in

# swapcase() swap the upper to lower and lower to upper
g = "I Love Python"
h = "i lOVE pYTHON"
print(g.swapcase())
print(h.swapcase())

# startwith() used in the logecal statments

i = "I Love Python"
print(i.startswith('I'))
print(i.startswith('S'))
print(i.startswith('P', 7, 12)) # you can also give it range

# endswith() is the same but for ending
i = "I Love Python"
print("_"*20)
print(i.endswith('n'))
print(i.endswith('s'))
print(i.endswith('e', 2, 6)) # you can also give it range

# index(text(substring), start, end)

a = ("I Love Python")
print(a.index("P")) # it gives you the location of the substring
print(a.index('P', 0,10)) # same cos it still in 7 and its inclouded in the range
#print(a.index("P", 0, 5)) this will through error cos its out of range

# find(text(substring), start, end) the difference is it will not give error if what you look for is not exist

a = ("I Love Python")
print(a.find("P")) # it gives you the location of the substring
print(a.find('P', 0,10)) # same cos it still in 7 and its inclouded in the range
print(a.find("P", 0, 5)) # when its not exist it will write -1

# rjust(width, fill character) ljust(same as rjust)
# its for right justifid and left justified
n = "Ahmed"
print(n.rjust(10)) # by defualt it will fill spaces
print(n.rjust(10, "*"))
print(n.ljust(10)) # by defualt it will fill spaces
print(n.ljust(10, "*"))

# splitlines()
e = """First Line
Second Line  
Third Line"""

print(e)
print(e.splitlines()) #it will return list each line is an item

f = "first line\nsecond line\nthird line"
print(f)

# expandtabs()
g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(10))
print(g.expandtabs(2))

#is(somthing)()
one = "I Love Python and 3g"
print(one.istitle()) #checks if the string is title
two = "I Love Python And 3G"
print(two.istitle())

three = ""
print(three.isspace())
four = "   "
print(four.isspace())

five = "i love python"
six = "I Love Pythin"
print(five.islower())
print(six.islower())

seven = "Ahmed_saleh" #checks if it possible to be variable name
eight = "Ahmed--saleh"
nine = "AhmedSaleh"
print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

x = "AaaaaaBbbbb" 
y = "AaaaaaBbbbb123"
print(x.isalpha()) # check if it only letters only
print(y.isalpha())

u = "AaaaaaBbbbb" 
z = "AaaaaaBbbbb123"
print(x.isalnum()) # check if it letters and numbers only
print(y.isalnum())

# replace(Old value, new value, count)

a = "Hello One Two Three One One"
print(a.replace("One","1"))
print(a.replace("One","1",1))

#join(Iterable)

mylist = ["Ahmed", "Saleh", "Mohammed"]
print("-".join(mylist))
print(" ".join(mylist))
print(",".join(mylist))
print("#".join(mylist))
