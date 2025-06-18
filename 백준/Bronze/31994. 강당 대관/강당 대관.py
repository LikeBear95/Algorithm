import sys
input = sys.stdin.readline

ms, mn = '', 0
for _ in range(7):
    s, n = map(str, input().split())
    if mn < int(n):
        ms = s
        mn = int(n)

print(ms)