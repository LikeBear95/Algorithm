def solution(dots):
    sqr = sorted(dots)
    answer = abs(sqr[0][0] - sqr[3][0]) * abs(sqr[0][1] - sqr[3][1])
    return answer