def solution(s):
    answer = []
    for i, w in enumerate(s):
        if w in s[:i]:
            for j in s[:i][::-1]:
                if j == w:
                    answer.append(s[:i][::-1].index(j) + 1)
                    break
        else:
            answer.append(-1)
    return answer