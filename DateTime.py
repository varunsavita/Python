import datetime

# Get the current data and time
now = datetime.datetime.now()
print(now)

# Get Current date

date = datetime.date.today()
print(date)

# dir() function to get a list
print(dir(datetime))

# Date object to represent a date
date = datetime.date(2023,12,25)
print(date)

# print today's year, month, and day
today = datetime.date.today()
print("Current year", today.year)
print("Current year", today.month)
print("Current year", today.day)

# time
time = datetime.time()
print(time)

# current date and time
now = datetime.datetime.now()

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)

