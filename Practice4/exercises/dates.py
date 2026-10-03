from datetime import datetime, timedelta

# Task 1
print(datetime.now() - timedelta(days=5))

# Task 2
today = datetime.now().date()
print("Yesterday:", today - timedelta(days=1))
print("Today:", today)
print("Tomorrow:", today + timedelta(days=1))

# Task 3
print(datetime.now().replace(microsecond=0))

# Task 4
date1 = datetime(2026, 9, 20, 10, 0, 0)
date2 = datetime(2026, 9, 27, 18, 0, 0)
print((date2 - date1).total_seconds())