def solution(lines):
    answer = 0
    x = [x[0] for x in lines]
    y = [y[1] for y in lines]
    tmp = [0] * (max(y) - min(x) + 1)
    num = [i for i in range(min(x), max(y) + 1)]
    for dot in lines:
        s, e = dot
        for i in range(s, e):
            tmp[num.index(i)] += 1
    for result in tmp:
        if result > 1:
            answer += 1
    return answer