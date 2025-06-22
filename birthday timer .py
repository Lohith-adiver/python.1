print("Name   : Lohith Adiver")
print("USN    : 1AY24AI063")
print("Section: O")

from datetime import datetime, timedelta

# 1. Current day of the week
today = datetime.now()
print("Today is:", today.strftime('%A'))

# 2. Age and time until next birthday
bday_input = input("Enter your birthday (YYYY-MM-DD): ")
bday = datetime.strptime(bday_input, "%Y-%m-%d")
age = today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day))
print("Your age is:", age)

next_bday = bday.replace(year=today.year)
if next_bday < today:
    next_bday = next_bday.replace(year=today.year + 1)

time_remaining = next_bday - today
print("Time until next birthday:", time_remaining)

# 3. Double Day
def double_day(birth1, birth2):
    if birth1 > birth2:
        birth1, birth2 = birth2, birth1
    diff = birth2 - birth1
    return birth2 + diff

# 4. n-times older
def n_times_day(birth1, birth2, n):
    if birth1 > birth2:
        birth1, birth2 = birth2, birth1
    diff = birth2 - birth1
    days = diff.days / (n - 1)
    return birth2 + timedelta(days=days)


date1 = datetime.strptime(input("Enter first birth date (YYYY-MM-DD): "), "%Y-%m-%d")
date2 = datetime.strptime(input("Enter second birth date (YYYY-MM-DD): "), "%Y-%m-%d")

print("Double Day:", double_day(date1, date2).date())

n = float(input("Enter n (e.g., 3 for triple age): "))
print(f"{n}-times Day:", n_times_day(date1, date2, n).date())
