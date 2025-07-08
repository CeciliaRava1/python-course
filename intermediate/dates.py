from datetime import datetime

now = datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# Unique representation of a time
timestamp = now.timestamp()
print(timestamp)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)
year2026 = datetime(2026, 1, 1)  #year, month, day


from datetime import time

current_time = time()
current_time.hour