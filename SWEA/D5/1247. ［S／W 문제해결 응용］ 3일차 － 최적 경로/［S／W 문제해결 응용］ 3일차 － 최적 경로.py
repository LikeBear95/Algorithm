def f(i, N):
    global min_v
    if i == N:
        # 현재 경로의 총 거리를 계산하여 min_v와 비교해서 갱신합니다.
        s = dis[0][p[0]]  # 회사부터 첫 번째 고객까지의 거리
        for k in range(N-1):
            s += dis[p[k]][p[k+1]]  # 고객들 간의 거리를 더해줍니다.
        s += dis[p[N-1]][1]  # 마지막 고객부터 집까지의 거리
        if min_v > s:
            min_v = s
    else:
        for j in range(i, N):
            # 현재 인덱스 i와 j를 교환하여 순열을 생성합니다.
            p[i], p[j] = p[j], p[i]
            f(i + 1, N)  # 다음 위치로 이동하여 순열을 계속 생성합니다.
            p[i], p[j] = p[j], p[i]  # 백트래킹: 원래 순서로 되돌려줍니다.

# T: 테스트 케이스
T = int(input())
for t in range(1, T + 1):
    # N: 고객 수, lst: 회사, 집, 고객 좌표, dis: 좌표간 거리
    N = int(input())
    lst = list(map(int, input().split()))
    dis = [[0] * (N+2) for _ in range(N+2)]

    # 각 좌표 간의 거리를 계산하여 dis 배열에 저장합니다.
    for i in range(N+1):
        for j in range(i+1, N+2):
            dis[i][j] = abs(lst[i*2] - lst[j*2]) + abs(lst[i*2+1] - lst[j*2+1])
            dis[j][i] = dis[i][j]

    p = [i for i in range(2, N+2)]  # 순열을 생성하기 위한 초기값 설정
    min_v = 999999999  # 최소 거리를 저장할 변수 초기화
    f(0, N)  # 순열 생성을 시작합니다.

    print(f'#{t} {min_v}')  # 결과 출력
