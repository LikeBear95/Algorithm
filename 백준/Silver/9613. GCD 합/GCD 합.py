import math
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    l = list(map(int, input().split()))
    n, l = l[0], l[1:]
    x = 0
    
    for i in range(n):
        for j in range(i):
            x += math.gcd(l[i], l[j])

    print(x)