import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print(1)
else:
    num = 1
    for i in range(1, n+1):
        num *= i
    print(num)
