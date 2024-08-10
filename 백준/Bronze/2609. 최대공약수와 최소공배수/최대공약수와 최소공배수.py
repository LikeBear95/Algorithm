import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
gcd = math.gcd(n, m)

print(gcd)
print(n * m // gcd)
