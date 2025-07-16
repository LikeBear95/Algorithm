n = 1800
for _ in range(4):
    t = int(input())
    n -= t

print("Yes" if n >= 300 else "No")