n = 0
m = 0

for _ in range(10):
    o, i = map(int, input().split())
    n = n - o + i
    if n > 10000:
        m = 10000
        break
    if m < n:
        m = n

print(m)