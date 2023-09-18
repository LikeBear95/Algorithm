T = int(input())
for tc in range(1, T+1):
    # N: 직원수, B: 선반높이
    N, B = map(int, input().split())
    # H: 직원키, tops: 키합
    H = list(map(int, input().split()))
    tops = [0]

    # 키합 부분집합들
    for i in range(N):
        for j in range(len(tops)):
            temp = H[i] + tops[j]
            tops.append(temp)

    tops = list(set(tops))

    result = B
    for i in tops:
        if 0 <= i - B < result:
            result = i - B

    print(f'#{tc}', result)
