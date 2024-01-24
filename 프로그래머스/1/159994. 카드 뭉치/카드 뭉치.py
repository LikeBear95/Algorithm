def solution(cards1, cards2, goal):
    answer = 'Yes'
    tmp = [0, 0]
    for word in goal:
        if tmp[0] < len(cards1) and word == cards1[tmp[0]]:
            tmp[0] += 1
        elif tmp[1] < len(cards2) and word == cards2[tmp[1]]:
            tmp[1] += 1
        else:
            return 'No'
    return answer