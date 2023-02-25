import datetime, time
a=datetime.datetime(2023, 2, 23).timetuple()
b=datetime.datetime(2023, 2, 28).timetuple()
z=time.mktime(a)-time.mktime(b)
print(abs(z))