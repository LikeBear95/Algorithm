for i in range(int(input())):
    a, b = map(int, input().split())
    n = 0
    for i in range(a, b+1):
        n += str(i).count("0")
    print(n)