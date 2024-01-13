def solution(x):
    answer = True
    if x % sum([int(n) for n in str(x)]):
        answer = False
    return answer