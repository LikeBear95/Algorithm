def solution(rank, attendance):
    answer = 0
    tmp = []
    for i in range(len(rank)):
        if attendance[rank.index(i+1)]:
            tmp.append(rank.index(i+1))
        if len(tmp) == 3:
            break
    a, b, c = tmp
    return a * 10000 + b * 100 + c