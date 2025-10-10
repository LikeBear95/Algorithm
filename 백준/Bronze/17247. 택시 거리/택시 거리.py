n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
p = []

for i in range(n):
    for j in range(m):
        if l[i][j] == 1:
            p.append(i)
            p.append(j)

a, b, c, d = map(int, p)

print(abs(d-b)+abs(c-a))