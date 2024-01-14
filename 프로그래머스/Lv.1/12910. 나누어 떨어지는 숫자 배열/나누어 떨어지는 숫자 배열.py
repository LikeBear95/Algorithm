def solution(arr, divisor):
    answer = [x for x in arr if not x % divisor]
    if not answer:
        answer.append(-1)
    return sorted(answer) 