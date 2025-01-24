for i in range(int(input())):
    a, b = map(str, input().split())
    a = int(a)
    print(f'{b[:a-1]}{b[a:]}')