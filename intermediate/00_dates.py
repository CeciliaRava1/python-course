### dates ###

from datetime import datetime

now = datetime.now()
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

# Unique representation of a time
timestamp = now.timestamp()
# print(timestamp)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

# print_date(now)
year_2026 = datetime(2026, 1, 1)  #year, month, day


from datetime import time # hour
current_time = time(21, 6, 0)
# print(current_time.hour)
# print(current_time.minute)
# print(current_time.second)


from datetime import date # date
current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2025, 7, 8)
print(current_date.year)
print(current_date.month)
print(current_date.day)

# current_date = date(current_date.year, current_date.month + 1, current_date.day)
# print(current_date.year)


# Difference between two dates
diff = year_2026 - now
print(diff)
diff = year_2026.date() - current_date
print(diff)

from datetime import timedelta 
start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print(end_timedelta - start_timedelta) # sum, sub