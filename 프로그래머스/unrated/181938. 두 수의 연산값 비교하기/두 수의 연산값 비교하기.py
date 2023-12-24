def solution(a, b):
    tmp1 = int(str(a) + str(b))
    tmp2 = 2 * a * b
    answer = max(tmp1, tmp2)
    return answer