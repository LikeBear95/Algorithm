import sys
input = sys.stdin.readline

n = int(input())
sx, sy, ex, ey = map(int, input().split())
l = []
for _ in range(n):
    m = int(input())
    t = 0
    tx, ty = sx, sy
    for _ in range(m):
        x, y = map(int, input().split())
        t += abs(tx-x)+abs(ty-y)
        tx, ty = x, y
    t += abs(tx-ex)+abs(ty-ey) 
    l.append(t)

print(l.index((min(l)))+1)