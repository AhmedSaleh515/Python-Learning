first_number = int(input("enter the first number: "))
operator = input("enter an operator: +, -, *, /, % : ")
second_number = int(input("enter the second number: "))

if operator == '+':
    print((first_number + second_number))
elif operator == '-':
    print((first_number - second_number))
elif operator == '*':
    print((first_number * second_number))
elif operator == '/':
    print((first_number / second_number))        
elif operator == '%':
    print((first_number % second_number))
else:
    print("invalid operator")
