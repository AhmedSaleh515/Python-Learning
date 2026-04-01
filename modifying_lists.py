fruits = ['Pineapple','Banana','Apple','Melon']
print(fruits)

#added an element at the end
fruits.append('Kiwi') 
print("\n",fruits)

#insert an element at a specific index
fruits.insert(0,'Oeange') 
fruits.insert(25,'Peach') # if the index is longer than the list it will added at the end
print('\n',fruits)

#remove an element
fruits.remove('Melon')
print('\n',fruits)
#fruits.remove('Pear')    error cos there is no Pear

#remove and return what is removed
fruits.pop(3)
print('\n',fruits)

#edit a specific element
fruits[2] = 'Strawberry'
print('\n',fruits)
