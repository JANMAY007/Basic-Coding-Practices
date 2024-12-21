from datetime import datetime, timedelta

dt1 = datetime(2001, 3, 19) + timedelta(days=1, seconds=1000)
dt2 = datetime.now()
duration = dt2 - dt1
print(duration)
print("days", duration.days)
print("seconds", duration.seconds)
print("total seconds", duration.total_seconds())
