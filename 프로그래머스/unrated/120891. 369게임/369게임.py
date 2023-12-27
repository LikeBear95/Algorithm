def solution(order):
    answer = 0
    TSN = [3, 6, 9]
    for num in str(order):
        if int(num) in TSN:
            answer += 1
    return answer