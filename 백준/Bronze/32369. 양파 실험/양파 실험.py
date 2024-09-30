n, a, b = map(int, input().split())
A = 1
B = 1

for _ in range(n):
    A += a
    B += b

    if B == A:
        B -= 1
    elif B > A:
        tmp = A
        A = B
        B = tmp

print(A, B)