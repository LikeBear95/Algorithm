# T: 테스트 케이스
T = int(input())
for tc in range(1, T + 1):
    card = list(input())
    Sdeck = list(range(1, 14))
    Ddeck = list(range(1, 14))
    Hdeck = list(range(1, 14))
    Cdeck = list(range(1, 14))

    answer = []

    while card:
        simbol = card.pop(0)
        num = ''
        num += card.pop(0)
        num += card.pop(0)
        if simbol == 'S' and int(num) in Sdeck:
            Sdeck.remove(int(num))
        elif simbol == 'D' and int(num) in Ddeck:
            Ddeck.remove(int(num))
        elif simbol == 'H' and int(num) in Hdeck:
            Hdeck.remove(int(num))
        elif simbol == 'C' and int(num) in Cdeck:
            Cdeck.remove(int(num))
        else:
            answer.clear()
            answer.append('ERROR')
            break

    if 'ERROR' not in answer:
        answer.append(len(Sdeck))
        answer.append(len(Ddeck))
        answer.append(len(Hdeck))
        answer.append(len(Cdeck))

    print(f'#{tc}', *answer)
