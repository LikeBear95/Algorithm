n, m = map(int, input().split())
for i in range(1, n*m+1):
    if i % m:
        print(i, end=' ')
    else:
        print(i)