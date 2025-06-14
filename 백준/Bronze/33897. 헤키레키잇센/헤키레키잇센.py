n = int(input())
l = list(map(int, input().split()))
t = [l[0]]
c, m = 1, 0

for i in range(1, n):
    if t[-1] > l[i]:
        c += 1
        m = max(m, len(t))
        t = [l[i]]
    else:
        t.append(l[i])

print(c, max(m, len(t)))
