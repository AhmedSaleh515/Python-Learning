import datetime
# 1 print the current date and time
print(datetime.datetime.now(), "\n")
print("01"*20 + "\n")

# 2 print the current year - month - day 

print(datetime.datetime.now().year) #year
print(datetime.datetime.now().month)#month
print(datetime.datetime.now().day ,"\n")#Day

print("02"*20 + "\n")

# 3 Print Start and End of Date 

print (datetime.datetime.min)
print (datetime.datetime.max, "\n")

print("03"*20 + "\n")

# 4 Print the current time- hour- min- sec- microssec
print ( datetime.datetime.now().time())
print ( datetime.datetime.now().time().hour)
print ( datetime.datetime.now().time().minute)
print ( datetime.datetime.now().time().second)
print ( datetime.datetime.now().time().microsecond, "\n")

print("04"*20 + "\n")

# 5 Print start end time
print(datetime.time.min)
print(datetime.time.max, "\n")

print("05"*20 + "\n")

# 6 print specific date
print (datetime.datetime(2003,11,21), "\n")

print("06"*20 + "\n")


# 7 simple birthday calculator in days

myBirthday = datetime.datetime(2003,11,21)
datenow = datetime.datetime.now()

print(f"my birthday is {myBirthday} and date now is {datenow}")
print (f"I lived for {(datenow-myBirthday).days} Days" + "\n")

print("07"*20 + "\n")
# 8 Date formating  

myBirthday # its allready exists in 07 above
# check strftime.org for all the formats shortcuts
print (myBirthday)
print (myBirthday.strftime("%B")) 
print (myBirthday.strftime("%A")) 
print (myBirthday.strftime("%a")) 
print (myBirthday.strftime("%b")) 
print (myBirthday.strftime("%d %B %Y"), "\n") 

print("08"*20 + "\n")

