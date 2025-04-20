import sys
input = sys.stdin.readline

for _ in range(3):
    a, b, c, x, y, z = map(int, input().split())
    t = (x-a)*3600 + (y-b)*60 + (z-c)
    h = t // 3600
    m = t % 3600 // 60
    s = t % 60
    print(h, m, s)