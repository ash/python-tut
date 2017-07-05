import datetime

d = datetime.datetime(2017, 2, 1, 3, 4, 50)
print(d)

n = datetime.datetime.now()
diff = n - d
print(diff)

in5days = n + datetime.timedelta(days=5, hours=10)
print(in5days)
