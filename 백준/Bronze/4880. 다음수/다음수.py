while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    if b-a == c-b:
        print(f'AP {c+b-a}')
    elif b//a == c//b:
        print(f'GP {c*b//a}')
