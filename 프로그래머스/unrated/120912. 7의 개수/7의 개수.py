def solution(array):
    answer = 0
    for number in array:
        for num in str(number):
            if num == '7':
                answer += 1
    return answer