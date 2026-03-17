def tips (bill):
    tip_in_percent = 1
    if bill < 100:
        tip_in_percent = 10
    elif bill >= 100 and bill < 200:
        tip_in_percent = 15
    elif bill >= 200 and bill < 300:
        tip_in_percent = 20
    elif  bill >= 300:
        tip_in_percent = 25
        return tip_in_percent
    tip = tip_in_percent / 100 * bill 
    print("the tip of this bill is", tip,"$")
    print("the total bill is", tip + bill,"$")
    #Note : the tip system is 10% for bills less than $100,
    #15% for bills between $100 and $200,
    #20% for bills between $200 and $300,
    #and 25% for bills above $300.
tips(50)
tips(150)
tips(250)
tips(350)
