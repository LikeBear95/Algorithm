a, b, c = map(int, input().split())

if a == b and b == c:
    print(f'{10000 + a * 1000}')
elif a != b and b != c and c != a:
    print(f'{max(a,b,c) * 100}')
elif (a==b and a!=c) or (a==c and a!=b):
    print(f'{1000 + a * 100}')
elif (b==c and b!=a):
    print(f'{1000 + b * 100}')