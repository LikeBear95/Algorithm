import datetime

d, m = map(int, input().split())
print(datetime.date(2009, m, d).strftime("%A"))