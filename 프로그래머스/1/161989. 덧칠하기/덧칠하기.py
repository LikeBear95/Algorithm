def solution(n, m, section):
    answer = 0
    tmp = [0] * n
    for s in section:
        tmp[s-1] = 1
    for i in range(n):
        if tmp[i]:
            for j in range(m):
                if i + j >= n:
                    pass
                else:
                    tmp[i+j] = 0
            answer += 1
    return answer