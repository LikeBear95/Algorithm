for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    x = 0

    for i in l:
        x += i//k
    print(x)