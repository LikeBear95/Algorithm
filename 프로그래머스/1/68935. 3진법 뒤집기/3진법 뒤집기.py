def solution(n):
    answer = 0
    tmp = ''
    while (n):
        tmp += str(n % 3)
        n //= 3
    for i in range(len(tmp) - 1, -1, -1):
        answer += int(tmp[i]) * 3 ** (len(tmp) - 1 - i)
    return answer