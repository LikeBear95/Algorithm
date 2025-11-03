import sys
input = sys.stdin.readline

for i in range(int(input())):
    n, m = map(int, input().split())
    print(n+m-1)