import datetime

dt = datetime.datetime.now()
print(dt.hour)

dt = datetime.datetime.utcnow()
print(dt.hour)

print(type(dt))
print(dir(dt))

print(datetime.MAXYEAR)
print(dt.second)

print(dt.__str__()) # same as print(dt)


print(datetime.date.today())
print(datetime.date.today().year)

