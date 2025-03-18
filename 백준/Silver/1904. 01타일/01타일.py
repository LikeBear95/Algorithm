n = int(input())
a, b = 1, 2

if n == 1:
    print(a)
elif n == 2:
    print(b)
else:
    for _ in range(3, n+1):
        a, b = b, (a+b) % 15746
    print(b)
