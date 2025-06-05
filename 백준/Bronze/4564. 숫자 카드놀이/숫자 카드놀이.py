while True:
    n = int(input())
    if n == 0:
        break
    while len(str(n)) != 1:
        print(n, end=" ")
        t = [int(x) for x in str(n)]
        c = 1
        for i in t:
            c *= i
        n = c
    print(n)
