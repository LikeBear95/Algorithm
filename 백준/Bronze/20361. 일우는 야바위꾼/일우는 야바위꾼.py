import sys
input = sys.stdin.readline

n, x, k = map(int, input().split())
l = [0] * (n+1)
l[x] = 1

for _ in range(k):
    a, b = map(int, input().split())
    if l[a] or l[b]:
        l[a], l[b] = l[b], l[a]
    
print(l.index(1))