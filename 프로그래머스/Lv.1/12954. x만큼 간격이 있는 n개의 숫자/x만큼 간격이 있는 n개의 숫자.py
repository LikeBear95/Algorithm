def solution(x, n):
    answer = [x]
    while(n != 1):
        answer.append(answer[-1] + x)
        n -= 1
    return answer