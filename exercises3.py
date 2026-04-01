#exercise 1 is practice for lists
raw_names = ["  ahmed", "sara ", "  JOHN  ", "mOna"]
new_names = []
for name in raw_names:
    stripped_name = name.strip()
    formated_name = stripped_name.capitalize()
    new_names.append(formated_name)
print(new_names)
#doing the same thing using list comprehension
formated_names = [name.strip().capitalize() for name in raw_names]
print(formated_names)
#__________________________________________________________________#
inventory = [("Apple", 5), ("Banana", 2), ("Orange", 8), ("Grapes", 12)]
budget = int(input('What is your budget?: '))
for item in inventory:
    item_name, item_price = item
    if item_price<= budget:
        print('you can afford {} for ${}'.format(item_name, item_price))
# Instead of 'for item in inventory' then unpacking inside...
for name, price in inventory:
    if price <= budget:
        print(f"You can afford {name} for ${price}")
               
        


        