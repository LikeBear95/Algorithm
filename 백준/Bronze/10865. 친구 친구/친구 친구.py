import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    l[a].append(b)
    l[b].append(a)

for i in l[1:]:
    print(len(i))