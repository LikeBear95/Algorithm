from collections import deque

# 상하좌우 방향으로 이동하는 데 사용할 방향 벡터
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def BFS(r, c):
    q = deque()
    # 출발점 초기화
    q.append((r, c))
    flat[r][c] = 0  # 출발점의 최소 연료 소비량은 0

    while q:
        i, j = q.popleft()
        # 현재 위치에서 상하좌우로 이동을 시도합니다.
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            # 맵 범위 안에 있는지 확인합니다.
            if 0 <= ni < N and 0 <= nj < N:
                # 현재 위치에서 다음 위치로 이동할 때 소모되는 연료를 계산합니다.
                if not MAP[ni][nj]:
                    temp = flat[i][j]  # 높이가 0인 경우, 추가 연료 소모 없음
                else:
                    temp = flat[i][j] + int(MAP[ni][nj])  # 높이가 있는 경우, 높이 만큼 연료가 소모됨
                
                # 현재 위치에서 다음 위치로 가는 것이 더 적은 연료를 소모하는 경우에만 업데이트합니다.
                if temp < flat[ni][nj]:
                    flat[ni][nj] = temp  # 더 적은 연료 소모량으로 업데이트
                    q.append((ni, nj))  # 다음 위치를 큐에 추가하여 탐색을 계속합니다.

T = int(input())
for tc in range(1, T + 1):
    # N: 맵크기
    N = int(input())
    MAP = [input() for _ in range(N)]

    # flat: 진행하는 동안 최소 사용 연료
    flat = [[10000000] * N for _ in range(N)]  # 충분히 큰 값으로 초기화

    # 시작점에서 BFS 탐색을 시작합니다.
    BFS(0, 0)

    # 목적지에 도달한 경우, 목적지까지의 최소 연료 사용량이 저장됩니다.
    print(f'#{tc} {flat[N - 1][N - 1]}')  # 최종 결과 출력
