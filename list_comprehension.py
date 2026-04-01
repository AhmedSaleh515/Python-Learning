multiples = []
for x in range(1,11):
    multiples.append(x*7)
print(multiples)

#instead of all of this above we can write in single line using list comprehensive 
multiple = [x*7 for x in range(1,11)]
print(multiple)

#anothor example that list the whole number from 0 to 100 that accept divide by 3
z = [x for x in range(0,101) if x % 3 == 0]
print(z)