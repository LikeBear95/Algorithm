import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    l[a] += 1
    l[b] += 1

for i in l[1:]:
    print(i)