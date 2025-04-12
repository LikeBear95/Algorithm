import sys
input = sys.stdin.readline

n, x = map(int, input().split())
lst = []
for _ in range(n):
    s, t = map(int, input().split())
    if s+t <= x:
        lst.append([s, t])

print(sorted(lst)[-1][0] if lst else -1)