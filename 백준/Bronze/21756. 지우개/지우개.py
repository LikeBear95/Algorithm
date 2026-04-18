n = int(input())
l = [x for x in range(1, n+1)]

while len(l) > 1:
    l = [x for x in l[1::2]]

print(*l)