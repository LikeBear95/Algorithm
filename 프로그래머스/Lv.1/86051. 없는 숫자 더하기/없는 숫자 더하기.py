def solution(numbers):
    answer = 0
    for num in range(10):
        if not num in numbers:
            answer += num
    return answer