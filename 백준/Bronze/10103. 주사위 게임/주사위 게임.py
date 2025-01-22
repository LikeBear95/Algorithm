c, s = 100, 100
for i in range(int(input())):
    x, y = map(int, input().split())
    if x > y:
        s -= x
    elif x < y:
        c -= y

print(c)
print(s)