for _ in range(int(input())):
    n = int(input())
    l = []
    for i in range(1, n//2+1):
        if i != n-i:
            l.append(f'{i} {n-i}')
    print(f'Pairs for {n}:', ", ".join(l))
