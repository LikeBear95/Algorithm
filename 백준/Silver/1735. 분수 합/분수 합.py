import math
a, x = map(int, input().split())
b, y = map(int, input().split())

gcd1 = x*y // math.gcd(x, y)
gcd2 = math.gcd(a*gcd1//x + b*gcd1//y, gcd1)

print((a*gcd1//x + b*gcd1//y)//gcd2, gcd1//gcd2)
