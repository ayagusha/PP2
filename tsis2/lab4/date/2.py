import datetime
a=datetime.datetime.now()
b=datetime.timedelta(days=1)
print("Yesterday:", a-b)
print("Today:", a)
print("Tomorrow:", a+b)