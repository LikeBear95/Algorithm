a, b, c = map(int, input().split())

for i in range(1, 11):
    l = []
    for j in range(1, 11):
        if a*i + b*j == c:
            l.append(j)
    print(*l if l else "0")