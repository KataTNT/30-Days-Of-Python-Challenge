"""
Project: 30 Days Of Python challenge
Author (Original): Asabeneh Yetayeh (https://github.com/Asabeneh/30-Days-Of-Python)
Day: 16 - Python Date time (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/16_Day_Python_date_time/16_python_datetime.md)
Challenger: KataTNT
"""

## Exercises:
from datetime import datetime
# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
print(now)

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formatted_date = datetime.strftime(now, "%m/%d/%Y, %H:%M:%S")
print(formatted_date)

# 3. Today is 5 December, 2019. Change this time string to time.
date_string = '5 December, 2019'
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)

# 4. Calculate the time difference between now and new year.
new_year = datetime(year=2027, month=1, day=1, hour=0, minute=0, second=0)
print('The time difference between now and new year', new_year - now) 

# 5. Calculate the time difference between 1 January 1970 and now.
t1 = datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0)
print('The time difference between 1 January 1970 and now:', now - t1)

# 6. Think, what can you use the datetime module for? Examples:
# - Time series analysis
# - To get a timestamp of any activities in an application
# - Adding posts on a blog