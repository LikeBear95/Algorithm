T = int(input())
for t in range(1, T + 1):
    N = int(input())
    score = list(map(int, input().split()))

    score_dict = {}

    while score:
        temp = score.pop(0)
        if temp in score_dict:
            score_dict[temp] += 1
        else:
            score_dict[temp] = 1

    cnt_mx = max(score_dict.values())
    lst_mx = []
    for i in score_dict:
        if score_dict[i] == cnt_mx:
            lst_mx.append(i)

    answer = max(lst_mx)

    print(f'#{t} {answer}')
