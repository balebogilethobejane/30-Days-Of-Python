#Day16. 
from datetime import datetime
#1. 


today = datetime.now()
print(today)

day = today.day
current_day = today.day
current_month = today.month
current_year = today.year
current_hour = today.hour
current_minute = today.minute
timestamp = today.timestamp() 
print(f"Day: {current_day}, Month: {current_month}, Year: {current_year}")
print(f"Hour: {current_hour}, Minute: {current_minute}")
print(f"Timestamp: {timestamp}")

#2. 
formatted_date = today.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Formatted Date: {formatted_date}")

#3.
from datetime import datetime

date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(f"Date Object: {date_object}")

#4. 
now = datetime.now()

new_year = datetime(now.year + 1, 1, 1)
time_difference = new_year - now
print(f"Time until New Year: {time_difference}")

#5.
now = datetime.now()
epoch_start = datetime(1970, 1, 1)
time_difference = now - epoch_start
print(f"Time since 1 January 1970: {time_difference}")

#6.
