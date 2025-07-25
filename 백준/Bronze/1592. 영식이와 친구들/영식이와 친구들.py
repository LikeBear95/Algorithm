n, m, l = map(int, input().split())
lst = [1] + [0 for _ in range(n-1)]
c, t = 0, l
while m not in lst:
    lst[t] += 1
    c += 1
    t = (t+l)%n

print(c)