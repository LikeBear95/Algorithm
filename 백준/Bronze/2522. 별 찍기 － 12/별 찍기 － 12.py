n = int(input())
for i in range(n):
    print(f'{" "*(n-i-1)}{"*"*(i+1)}')

for j in range(n-1):
    print(f'{" "*(j+1)}{"*"*(n-j-1)}')