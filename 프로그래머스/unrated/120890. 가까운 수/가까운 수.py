def solution(array, n):
    answer = array[0]
    for num in array:
        if abs(n - answer) > abs(n - num):
            answer = num
        elif abs(n - answer) == abs(n - num):
            answer = min(answer, num)
    return answer