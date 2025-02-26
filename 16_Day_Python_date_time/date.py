from datetime import datetime

today = datetime.now()
print(today)

day = today.day
print(day)
timestamp = today.timestamp()
print('timestamp', timestamp)