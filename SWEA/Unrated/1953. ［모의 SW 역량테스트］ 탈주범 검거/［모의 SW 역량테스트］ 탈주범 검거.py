def escape(r, c, i, l):
    # 현재 위치를 방문했음을 표시
    visited[r][c] = 1
    # 방문한 위치를 집합에 추가
    esc.add((r,c))
    if i == l:
        return
    else:
        # 오른쪽으로 이동 가능한 경우
        if c+1 < M and MAP[r][c] in [1, 3, 4, 5] and MAP[r][c + 1] in [1, 3, 6, 7] and visited[r][c + 1] == 0:
            # 오른쪽으로 이동
            visited[r][c + 1] = 1
            escape(r, c + 1, i + 1, l)
            # 이동한 후 다시 원래 상태로 되돌림
            visited[r][c + 1] = 0
        # 아래쪽으로 이동 가능한 경우
        if r+1 < N and MAP[r][c] in [1, 2, 5, 6] and MAP[r + 1][c] in [1, 2, 4, 7] and visited[r + 1][c] == 0:
            visited[r + 1][c] = 1
            escape(r + 1, c, i + 1, l)
            visited[r + 1][c] = 0
        # 왼쪽으로 이동 가능한 경우
        if c-1 >= 0 and MAP[r][c] in [1, 3, 6, 7] and MAP[r][c - 1] in [1, 3, 4, 5] and visited[r][c - 1] == 0:
            visited[r][c - 1] = 1
            escape(r, c - 1, i + 1, l)
            visited[r][c - 1] = 0
        # 위쪽으로 이동 가능한 경우
        if r-1 >= 0 and MAP[r][c] in [1, 2, 4, 7] and MAP[r - 1][c] in [1, 2, 5, 6] and visited[r - 1][c] == 0:
            visited[r - 1][c] = 1
            escape(r - 1, c, i + 1, l)
            visited[r - 1][c] = 0

# T: 테스트 케이스
T = int(input())
for t in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    esc = set()

    escape(R, C, 1, L)
    answer = len(esc)

    print(f'#{t} {answer}')  # 결과 출력
