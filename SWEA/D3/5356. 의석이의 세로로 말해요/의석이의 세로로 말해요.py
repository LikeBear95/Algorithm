# T: 테스트 케이스
T = int(input())
for tc in range(1, T + 1):
    word = [list(input()) for _ in range(5)]

    mx_len = 0
    for i in range(5):
        if mx_len < len(word[i]):
            mx_len = len(word[i])

    answer = ''
    for j in range(mx_len):
        for i in range(5):
            try:
                answer += word[i][j]
            except:
                continue

    print(f'#{tc} {answer}')
    