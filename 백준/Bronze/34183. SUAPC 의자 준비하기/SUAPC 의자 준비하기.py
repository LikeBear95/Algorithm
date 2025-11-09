n, m, a, b = map(int, input().split())
print(0 if 3*n<=m else (3*n-m)*a+b)