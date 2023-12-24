def solution(n):
    answer = 0
    for num in range(1, n+1):
        tmp = []
        for i in range(1, num+1):
            if num % i == 0:
                tmp.append(i)
        if len(tmp) >= 3:
            answer += 1
    return answer