n = int(input())
for i in range(1, n+1):
    if i == 1:
        print(f'{" "*(n-1)}*')
    else:
        print(f'{" "*(n-i)}*{" "*(2*i-3)}*')