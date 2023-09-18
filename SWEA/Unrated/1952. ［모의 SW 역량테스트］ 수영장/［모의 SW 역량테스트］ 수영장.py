T = int(input())
for tc in range(1, T+1):
    # D: 1일, M: 1달, T: 3달, Y: 1년 요금
    D, M, T, Y = map(int, input().split())
    # swim: 이용횟수, cost: 요금
    swim = list(map(int, input().split()))
    cost = [0] * 13

    for i in range(1, 13):
        temp = [0, M, T, Y]
        temp[0] = cost[i - 1] + swim[i - 1] * D
        temp[1] = cost[i - 1] + M
        if i >= 3:
            temp[2] = cost[i - 3] + T

        cost[i] = min(temp)

    answer = cost[12]

    print(f'#{tc}', answer)
