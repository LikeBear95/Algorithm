n = int(input())
l = list(map(int, input().split()))
c, m = 0, 0

for i in l:
    if i:
        c += 1
    else:
        m = max(m, c)
        c = 0

print(max(m, c))