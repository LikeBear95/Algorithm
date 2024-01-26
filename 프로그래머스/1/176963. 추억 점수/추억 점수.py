def solution(name, yearning, photo):
    answer = []
    for lst in photo:
        tmp = 0
        for n, y in zip(name, yearning):
            tmp += lst.count(n) * y
        answer.append(tmp)
    return answer