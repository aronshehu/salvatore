def days_in_month(year, month):
    if month == 2:
        return 28
    elif month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    else:
        return "invalid"
print(days_in_month(2007, 9))

def day_in_week(year, month, day):
    if month == 1:
        month = 13
        year = year - 1
    elif month == 2:
        month = 14
        year = year - 1
k = year % 100
j = year // 100

h = (day + (13 * (month + 1)) // 5 + k + (k // 4) + (j // 4) + 5 * j) % 7

if h == 0:
    return "Saturday"
elif h == 1:
    return "Sunday"
elif h == 2:
    return "Monday"
elif h == 3:
    return "Tuesday"
elif h== 4:
    return "Wednesday"
elif h==5:
    return "Thursday"
else:
    return "Friday"

print(day_in_week(2026, 1, 26))

def prime_nr(a):
    if a <= 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True
