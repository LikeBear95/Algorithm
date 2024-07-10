import sys
import math
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
num = 1

for i in range(n):
    num = num * lst[i] // math.gcd(num, lst[i])

print(num * min(lst) if num in lst else num)
