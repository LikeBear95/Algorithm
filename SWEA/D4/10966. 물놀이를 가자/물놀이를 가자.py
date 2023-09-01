from collections import deque
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# T: 테스트 케이스
for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    MAP = [input() for _ in range(N)]

    move = [[-1] * M for _ in range(N)]

    queue = deque()
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 'W':
                queue.append((i, j))
                move[i][j] = 0

    res = 0
    while queue:
        temp = queue.popleft()
        r, c = temp[0], temp[1]

        for k in range(4):
            nr, nc = r + drc[k][0], c + drc[k][1]
            if 0 <= nr < N and 0 <= nc < M and MAP[nr][nc] == 'L' and move[nr][nc] == -1:
                move[nr][nc] = move[r][c] + 1
                res += move[nr][nc]
                queue.append((nr, nc))

    print(f'#{t} {res}')  # 결과 출력
