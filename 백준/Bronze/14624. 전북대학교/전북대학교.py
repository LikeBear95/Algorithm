n = int(input())
if n%2:
    print(f'{"*"*n}')
    print(f'{" "*(n//2)}*')
    for i in range(n//2):
        print(f'{" "*(n//2-i-1)}*{" "*(2*i+1)}*')
else:
    print("I LOVE CBNU")