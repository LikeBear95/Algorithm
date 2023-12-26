def solution(s):
    numbers = list(map(str, s.split()))
    answer = 0
    for i, tmp in enumerate(numbers):
        if tmp == 'Z':
            answer -= int(numbers[i - 1])
        else:
            answer += int(tmp)
    return answer