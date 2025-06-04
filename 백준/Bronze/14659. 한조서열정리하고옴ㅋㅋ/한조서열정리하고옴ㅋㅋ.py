n = int(input())
l = list(map(int, input().split()))
h, c, m = 0, 0, 0

for i in l:
    if h < i:
        h = i
        m = max(m, c)
        c = 0
    else:
        c += 1

m = max(m, c)
print(m)