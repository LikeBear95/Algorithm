n = int(input())
for i in range(n):
    print(f'{" "*i}{"*"*(2*(n-i)-1)}')
for i in range(n-2, -1, -1):
    print(f'{" "*i}{"*"*(2*(n-i)-1)}')