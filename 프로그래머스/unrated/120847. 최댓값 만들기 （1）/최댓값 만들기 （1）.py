def solution(numbers):
    numbers.sort()
    answer = numbers[-1] * numbers[-2]
    # tmp1 = numbers.pop(numbers.index(max(numbers)))
    # tmp2 = numbers.pop(numbers.index(max(numbers)))
    # answer = tmp1 * tmp2
    return answer