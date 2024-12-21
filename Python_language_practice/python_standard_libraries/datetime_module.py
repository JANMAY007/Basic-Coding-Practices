from datetime import datetime
import time

dt1 = datetime(2001, 3, 19)
dt2 = datetime.now()
dt3 = datetime.strptime("19/03/2001", "%d/%m/%Y")
dt4 = datetime.fromtimestamp(time.time())
dt5 = dt4.strftime("%Y/%m/%d")
print(dt1)
print(dt2)
print(dt3)
print(dt4)
print(dt5)
print(dt1 > dt2)
