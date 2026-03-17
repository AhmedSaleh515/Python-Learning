#odd-even
"""def odd_or_even(num):
    if num % 2 == 0 :
      print ("Your number is Even!!")
    else:
       print ("Your number is Odd")  
number = int(input("inter the number you want to check on: ")  )
odd_or_even(number)"""
#--------------------------------------------------------------------#
# loop creat product table for the number user want and ask him if he wanna find another table before stop

def product_table (status):
   for x in range(10+1):
      print(status,"x",x,"=",str(status*x))
desire = input("Are you looking for product table for a specific Number (N) for Not (Y) for Yes:")
while desire == 'Y':
    test = int(input("Enter a Number you want to see it product Table :"))
    product_table(test)
    desire = input("Are you still need to see another table: ")
print('see you soon')
#--------------------------------------------------------------------#
#this code is an improved from the one above build by AI i did ask it to show me a way better than mine
"""def product_table(num):
    # Using range(1, 11) starts at 1 and ends at 10
    for x in range(1, 11):
        print(f"{num} x {x} = {num * x}")

# .upper() makes sure 'y' or 'Y' both work!
desire = input("Do you want a table? (Y/N): ").upper()

while desire == 'Y':
    test = int(input("Enter a Number: "))
    product_table(test)
    desire = input("See another table? (Y/N): ").upper()

print("Goodbye!")"""
    
        