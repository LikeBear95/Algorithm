di = [0, 1, 1, 1]
dj = [1, 1, 0, -1]

# T: 테스트 케이스
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    MAP = [list(input()) for _ in range(N)]
    answer = 'NO'

    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 'o':
                for k in range(4):
                    for m in range(1, 5):
                        ni, nj = i + di[k] * m, j + dj[k] * m
                        if 0 <= ni < N and 0 <= nj < N and MAP[ni][nj] == 'o':
                            pass
                        else:
                            break
                    else:
                        answer = 'YES'
                        break

    print(f'#{tc} {answer}')
    