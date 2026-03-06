i = 1

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    print(f'Triangle #{i}')
    i += 1
    
    if c == -1:
        print(f'c = {(a**2+b**2)**0.5:.3f}')
    else:
        if c<=a or c<=b:
            print('Impossible.')
        else:
            print(f'{"a" if a==-1 else "b"} = {(c**2-a**2-b**2+1)**0.5:.3f}')
    print()