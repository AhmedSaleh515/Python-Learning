import datetime

year = int(input("year of birth: "))
month = int(input("month of birth: "))
day = int(input("day of birth: "))
print("__"*20,"\n")

birthday = datetime.datetime(year,month,day)
date_now = datetime.datetime.now()

diff = date_now - birthday #difference 
ageInYears = diff.days//365
remaining_days_after_years = diff.days % 365
months = int(remaining_days_after_years // 30.44)
days = int(remaining_days_after_years % 30.44)

print(f"Your age is {ageInYears} years and {months} months and {days} days")

monthsToBirthday = month - date_now.month 
months_to_birthday = month - date_now.month
days_to_birthday = day - date_now.day

if days_to_birthday < 0:
    months_to_birthday -= 1
    days_to_birthday += 30 

if months_to_birthday < 0:
    months_to_birthday += 12

if monthsToBirthday == 0 and days_to_birthday == 0:
    print("Happy Birth Day!!")
else:
    print(f"Your next birthday is after {months_to_birthday} months and {days_to_birthday} days")
    