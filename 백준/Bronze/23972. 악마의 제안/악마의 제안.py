k, n = map(int, input().split())
if n == 1:
    x = -1
else:
    x = (n*k+n-2)//(n-1)

print(x)