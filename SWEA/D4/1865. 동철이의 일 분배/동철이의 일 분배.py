def backtracking(cnt, chan):
    global answer
    # 기저 조건
    # 숫자 N개를 골랐을 때 종료
    if cnt == N:
        answer = chan * 100
        return

    for num in arr:
        # 가지치기 - 중복된 숫자 제거
        # 조건을 작성하는 것이 핵심
        if num in path or chan * P[cnt][num] <= answer:
            continue
        chan *= P[cnt][num] * 0.01
        # 들어가기 전 로직 - 경로 저장
        path[cnt] = num
        # 다음 재귀 함수 호출
        backtracking(cnt + 1, chan)
        # 돌아와서 할 로직
        path[cnt] = -1
        chan /= P[cnt][num] * 0.01

T = int(input())
for tc in range(1, T+1):
    # N: 인원, 일 수, P: 확률
    N = int(input())
    P = []
    for i in range(N):
        P.append(list(map(int, input().split())))

    arr = [i for i in range(N)]
    path = [-1] * N

    answer = 0
    backtracking(0, 1)

    print(f'#{tc} {answer:.6f}')
