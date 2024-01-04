def solution(a, b):
    answer = 2
    while(b):
        if b % 2 == 0:
            b //= 2
        elif b % 5 == 0:
            b //= 5
        else:
            break
    if a % b == 0:
        answer = 1
    return answer