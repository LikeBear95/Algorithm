def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        if num ** (1/2) == int(num ** (1/2)):
            answer -= num
        else:
            answer += num
    return answer