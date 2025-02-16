x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

d1 = (x2-x1)**2 + (y2-y1)**2
d2 = (r1+r2)**2

print("YES" if d1 < d2 else "NO")