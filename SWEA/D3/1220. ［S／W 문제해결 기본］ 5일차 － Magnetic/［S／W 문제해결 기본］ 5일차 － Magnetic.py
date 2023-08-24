# T: 테스트 케이스
T = 10
for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for i in range(N):
        lst = ''
        for j in range(N):
            if MAP[j][i]:
                lst += str(MAP[j][i])
        # print(lst)
        for k in range(len(lst)-1):
            # print(lst[k:k+2])
            if lst[k:k+2] == '12':
                answer += 1

    print(f'#{tc} {answer}')
