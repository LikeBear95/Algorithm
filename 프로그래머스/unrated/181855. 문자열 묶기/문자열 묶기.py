def solution(strArr):
    tmp = [0] * 31
    for Arr in strArr:
        tmp[len(Arr)] += 1
    return max(tmp)