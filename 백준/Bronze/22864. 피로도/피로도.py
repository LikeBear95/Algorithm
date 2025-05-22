a, b, c, m = map(int, input().split())
n, t = 0, 0

for _ in range(24):
    if n+a <= m:
        n += a
        t += b
    else:
        n = n-c if n>c else 0

print(t)