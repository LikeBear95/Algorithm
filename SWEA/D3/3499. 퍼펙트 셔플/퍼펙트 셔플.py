# T: 테스트 케이스
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    card = list(input().split())
    deck1 = card[0:(N-1)//2+1]
    deck2 = card[(N-1)//2+1:N]
    answer = []

    for i in range(1, N + 1):
        if i % 2:
            answer.append(deck1.pop(0))
        else:
            answer.append(deck2.pop(0))

    print(f'#{tc}', *answer)
