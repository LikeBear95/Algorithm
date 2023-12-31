def solution(n):
    answer = 2
    for num in range(n):
        if num ** 2 == n:
            answer = 1
            break
        elif num ** 2 > n:
            break
    return answer