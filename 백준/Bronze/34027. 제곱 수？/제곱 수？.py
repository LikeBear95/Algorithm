import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    print(1 if n**(1/2) == int(n**(1/2)) else 0)