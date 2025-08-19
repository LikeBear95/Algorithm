c, k = map(int, input().split())
m = 10**k
ans = ((c + m//2) // m) * m
print(ans)
