a, b = 0, 0

for _ in range(10):
    n = int(input())
    a, b = b, b + n
    if b >= 100:
        break

print(a if abs(100-a)<abs(100-b) else b)