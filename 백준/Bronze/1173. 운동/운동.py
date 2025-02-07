N, m, M, T, R = map(int, input().split())
X = m
n = 0

while N > 0:
    n += 1
    if X+T > M:
        if X == m:
            n = -1
            break
        else:
            X = m if X-R < m else X-R
    else:
        X += T
        N -= 1

print(n)