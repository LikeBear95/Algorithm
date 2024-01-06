def solution(i, j, k):
    answer = 0
    numbers = list(range(i, j+1))
    for num in numbers:
        answer += str(num).count(str(k))
    return answer