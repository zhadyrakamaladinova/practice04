from datetime import datetime, timedelta, date

# 1. Subtract five days from current date
today = date.today()
print(today - timedelta(days=5))

# 2. Yesterday, today, tomorrow
print(today - timedelta(days=1))
print(today)
print(today + timedelta(days=1))

# 3. Drop microseconds from datetime
now = datetime.now()
print(now.replace(microsecond=0))

# 4. Difference between two dates in seconds
d1 = datetime(2025, 1, 1)
d2 = datetime(2025, 3, 15, 12, 30)
print(int((d2 - d1).total_seconds()))