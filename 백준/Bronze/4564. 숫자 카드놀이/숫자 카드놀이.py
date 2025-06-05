while True:
    n = int(input())
    if n == 0:
        break
    while len(str(n)) != 1:
        print(n, end=" ")
        t = 1
        for i in [int(x) for x in str(n)]:
            t *= i
        n = t
    print(n)
