n, x = map(int, input().split())
s = sum(map(int, input().split()))

i = x*n - s

if i <= 0:
    print(0)
else:
    print((i + (100-x) - 1) // (100-x))
