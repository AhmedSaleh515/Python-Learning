def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def day_of_year(year, month, day):
    cum_days_before = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    # index 0 unused, month 1 = Jan → cum_days_before[1] = 31? Wait, careful.
    
    # Let's define correctly: cum_days_before[m] = total days in months 1..m-1
    cum_days_before = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    # cum_days_before[1] = 0 (before Jan), cum_days_before[2] = 31 (before Feb), etc.
    
    day_num = cum_days_before[month] + day
    
    if is_leap(year) and month > 2:
        day_num += 1
        
    return day_num

# Example
year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

result = day_of_year(year, month, day)
print(f"{year}-{month:02d}-{day:02d} is day number {result} of the year.")