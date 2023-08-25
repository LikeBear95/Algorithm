def scan():
    answer = 0
    K = N + 1   # 맵을 다 덮을 범위

    for k in range(K, 0, -1):
        cost = k*k + (k-1)*(k-1)

        for i in range(N):
            for j in range(N):
                count = 0
                for ni, nj in house:
                    distance = abs(ni-i) + abs(nj-j)
                    if distance < k:
                        count += 1
                if count * M >= cost:
                    answer = max(answer, count)
        if answer != 0:
            return answer
    return answer

# T: 테스트 케이스
T = int(input())
for tc in range(1, T + 1):
    # N: 도시의 크기, M: 비용
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    house = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                house.append([i, j])

    # 아이디어 : 우선 맵을 다 덮을 범위만큼 영역 잡기
    # 한 집을 기준으로 범위 안에 다른 집들이 있으면 카운트,
    # 카운트된 집들과 영역 가격 비교
    answer = scan()

    print(f'#{tc} {answer}')
    # for i in range(N):
    #     for j in range(N):
    #         print(arr[i][j], end= "")
    #     print()
