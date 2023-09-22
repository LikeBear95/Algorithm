import heapq

# 최소 신장 트리(Minimum Spanning Tree)를 구하는 함수
def prim(start):
    heap = []  # 우선순위 큐로 사용할 리스트
    MST = [0] * N  # 최소 신장 트리에 포함된 정점을 표시하는 리스트

    heapq.heappush(heap, (0, start))  # 시작 정점을 힙에 추가, 초기 거리는 0
    total = 0  # MST의 총 가중치를 저장하는 변수

    while heap:
        distance, v = heapq.heappop(heap)  # 힙에서 가장 가까운 정점을 꺼냄

        if MST[v]:  # 이미 최소 신장 트리에 포함된 정점인 경우
            continue

        MST[v] = 1  # 최소 신장 트리에 포함시킴

        total += distance  # MST의 총 가중치에 현재 간선의 가중치를 더함

        # 현재 정점과 연결된 모든 정점을 고려
        for nxt in range(N):
            if dist[v][nxt] == 0 or MST[nxt]:  # 이미 포함되었거나 연결되지 않은 정점은 무시
                continue

            heapq.heappush(heap, (dist[v][nxt], nxt))  # 다음에 탐색할 정점과 가중치를 힙에 추가

    return total  # 최소 신장 트리의 총 가중치 반환

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 정점의 개수

    x_lst = list(map(int, input().split()))  # x 좌표 리스트
    y_lst = list(map(int, input().split()))  # y 좌표 리스트

    dist = [[0] * N for _ in range(N)]  # 정점 간 거리를 저장하는 2차원 리스트

    island = []
    # 모든 정점 간의 거리를 계산하고 저장
    for i in range(N - 1):
        for j in range(i + 1, N):
            dist[i][j] = (x_lst[i] - x_lst[j]) ** 2 + (y_lst[i] - y_lst[j]) ** 2
            dist[j][i] = dist[i][j]
            island.append((i, j, dist[i][j]))  # (정점1, 정점2, 거리) 정보를 리스트에 저장

    E = float(input())  # 환경 부담 세율

    # 환경 부담금을 곱한 후 반올림하여 결과 출력
    print(f'#{tc} {round(E * prim(0))}')
