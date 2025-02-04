for _ in range(int(input())):
    a, b, c, x, y, z = map(int, input().split())
    d = (x-a)**2 + (y-b)**2
    r1 = (c+z)**2
    r2 = (c-z)**2
    if d == 0:
        if c == z:
            print(-1)
        else:
            print(0)
    elif d > r1 or d < r2:
        print(0)
    elif d == r1 or d == r2:
        print(1)
    else:
        print(2)