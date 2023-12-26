def solution(strArr):
    answer = []
    for i, string in enumerate(strArr):
        if i % 2:
            answer.append(string.upper())
        else:
            answer.append(string.lower())
    return answer