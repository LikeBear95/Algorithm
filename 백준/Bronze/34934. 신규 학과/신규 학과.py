import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s, n = map(str, input().split())
    if int(n) == 2026:
        print(s)
        break