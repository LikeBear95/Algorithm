x = '6789012345'
y = 'IJKLABCDEFGH'
n = int(input())

print(f'{y[n%12]}{x[n%10]}')