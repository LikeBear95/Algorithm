def solution(before, after):
    answer = 0
    for alpha in before:
        if before.count(alpha) != after.count(alpha):
            break
    else:
        answer = 1
    return answer