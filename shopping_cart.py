cart = []
total = 0

while True :
     item = input('what do you need-if you finish write done-:').strip().lower()
     if item != 'done':
          price = float(input('how much you need in doller: '))
          chosen_item = (item, price)
          cart.append(chosen_item)
     else:
          break
if cart == []:
     print('You bought nothing')  
else:
     print('\n--- YOUR RECEIPT ---')
     for iitem, pprice in cart:
          print(f'- {iitem.capitalize()}: ${pprice:.2f}')
          total += pprice # Adding each price to the total
     
     print("-" * 20)
     print(f'TOTAL BILL: ${total:.2f}')

                       
     
     