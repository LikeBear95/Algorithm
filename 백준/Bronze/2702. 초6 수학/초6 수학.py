import math

for _ in range(int(input())):
    a, b = map(int, input().split())
    n = math.gcd(a, b)
    print(a*b//n, n)