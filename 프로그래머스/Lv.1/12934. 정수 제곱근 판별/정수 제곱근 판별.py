def solution(n):
    answer = 0
    while(answer ** 2 < n):
        answer += 1
    if answer ** 2 > n:
        answer = -1
    else:
        answer = (answer + 1) ** 2
    return answer