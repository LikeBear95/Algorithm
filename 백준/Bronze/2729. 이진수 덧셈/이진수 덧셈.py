for _ in range(int(input())):
    x, y = map(str, input().split())
    print(bin(int(x, 2) + int(y, 2))[2:])