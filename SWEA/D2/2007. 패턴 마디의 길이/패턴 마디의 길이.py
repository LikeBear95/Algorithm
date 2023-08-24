# T: 테스트 케이스
T = int(input())
for tc in range(1, T + 1):
    word = input()
    answer = 0

    for i in range(1, len(word)):
        if word[0:i] == word[i:i*2]:
            answer = len(word[0:i])
            break

    print(f'#{tc} {answer}')
