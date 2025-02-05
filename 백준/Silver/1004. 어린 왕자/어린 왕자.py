for i in range(int(input())):
    n = 0
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(int(input())):
        cx, cy, r = map(int, input().split())
        d1 = (x1-cx)**2 + (y1-cy)**2 > r**2
        d2 = (x2-cx)**2 + (y2-cy)**2 > r**2
        if d1 != d2:
            n += 1
    print(n)