#Empty list to fill later
my_favourit_webs = []
maximum_webs = 5

while maximum_webs > 0 :
    new_website = input('Enter your favourit website: ')
    my_favourit_webs.append(f"https://{new_website.strip().lower()}")
    maximum_webs -= 1
    print(f"website added, {maximum_webs} Place Left")
print(my_favourit_webs)    