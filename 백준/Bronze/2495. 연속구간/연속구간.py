for _ in range(3):
    n = int(input())
    t, c, m = 0, 0, 0
    for i in str(n):
        if t == i:
            c += 1
        else:
            m = max(c, m)
            t = i
            c = 1
    print(max(c, m))