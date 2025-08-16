a, b = map(int, input().split())
k, x = map(int, input().split())
c = 0

for i in range(a, b+1):
    if abs(k-i) <= x:
        c += 1

print(c if c else "IMPOSSIBLE")