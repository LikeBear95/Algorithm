a, b = map(int, input().split())

if (a+b)%2 != 0 or (a-b)%2 != 0:
    print(-1)
else:
    x = (a+b)//2
    y = (a-b)//2

    if x < 0 or y < 0:
        print(-1)
    else:
        print(max(x, y), min(x, y))
