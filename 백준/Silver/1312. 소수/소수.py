a, b, n = map(int, input().split())
a *= 10**n
print(str(a//b)[-1])