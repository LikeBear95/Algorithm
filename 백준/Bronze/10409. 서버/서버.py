n, t = map(int, input().split())
l = list(map(int, input().split()))
c, s = 0, 0

for i in l:
    if s+i <= t:
        c += 1
        s += i
    else:
        break

print(c)