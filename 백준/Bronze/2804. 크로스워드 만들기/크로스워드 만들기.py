a, b = map(str, input().split())
n, m = len(a), len(b)
x, y = -1, -1

for i in range(n):
    for j in range(m):
        if a[i] == b[j]:
            x, y = i, j
            break
    if x != -1:
        break

for j in range(m):
    for i in range(n):
        if i == x:
            print(b[j], end='')
        elif j == y:
            print(a[i], end='')
        else:
            print(".", end='')
    print()
