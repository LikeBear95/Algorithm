def solution(n, k):
    answer = 12000 * n
    if k - n // 10 > 0:
        answer += (k - n // 10) * 2000
    return answer