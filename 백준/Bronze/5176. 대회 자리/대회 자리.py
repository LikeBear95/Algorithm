for i in range(int(input())):
    p, m = map(int, input().split())
    lst = set()
    n = 0
    for j in range(p):
        x = int(input())
        if x in lst:
            n += 1
        else:
            lst.add(x)
    print(n)
    