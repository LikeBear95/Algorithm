def solution(numbers):
    tmp = sorted(numbers)
    answer = max(tmp[0]*tmp[1], tmp[-1]*tmp[-2])
    return answer