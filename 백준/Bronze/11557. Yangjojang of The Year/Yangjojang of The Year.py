for i in range(int(input())):
    s = []
    b = []
    for j in range(int(input())):
        x, y = map(str, input().split())
        s.append(x)
        b.append(int(y))
    print(s[b.index(max(b))])