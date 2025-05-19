n = int(input())
a, b = 1, 5000
for _ in range(n):
    t, n = map(int, input().split())
    a = max(a, t)
    b = min(b, n)

print(a*b%7+1)