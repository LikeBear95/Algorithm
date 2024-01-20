def solution(sizes):
    tmp1 = []
    tmp2 = []
    for i in sizes:
        tmp1.append(max(i))
        tmp2.append(min(i))
    answer = max(tmp1) * max(tmp2)
    return answer