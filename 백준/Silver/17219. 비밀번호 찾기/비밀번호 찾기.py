import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = {}

for _ in range(n):
    s, p = map(str, input().rstrip().split())
    d[s] = p

for _ in range(m):
    t = input().rstrip()
    print(d.get(t))