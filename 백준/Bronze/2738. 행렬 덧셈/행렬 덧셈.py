N, M = map(int, input().split())
lst = [[0] * M for _ in range(N)]
for _ in range(2):
    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in range(M):
            lst[i][j] += tmp[j]

for i in range(N):
    print(*lst[i])