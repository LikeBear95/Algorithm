for _ in range(int(input())):
    n = int(input())

    print(f'{"#"*n}')

    if n >= 2:
        for _ in range(n-2):
            print(f'#{"J"*(n-2)}#')
        print(f'{"#"*n}')
    print()