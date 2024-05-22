n, m = map(int, input().split())
chess = [input() for x in range(n)]
lst = []

for i in range(n-7):
    for j in range(m-7):
        cnt = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b + 1) % 2 and chess[a][b] != chess[i][j]:
                    cnt += 1
                elif (a + b) % 2 and chess[a][b] == chess[i][j]:
                    cnt += 1
        if cnt > 32:
            lst.append(64 - cnt)
        else:
            lst.append(cnt)

print(min(lst))
