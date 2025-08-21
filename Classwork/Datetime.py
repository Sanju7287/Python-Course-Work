from datetime import date, time, datetime, timedelta
today=date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.isoweekday())

d=date(2025,8,31)
print(d)

t=time(13,29,20)
print(t)

now=datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

