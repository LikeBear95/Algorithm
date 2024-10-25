a, b = map(int, input().split())
d = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

while a != 1:
    if a == 3:
        b += 28
    elif a in [5, 7, 10, 12]:
        b += 30
    else:
        b += 31
    a -= 1

print(d[b%7])