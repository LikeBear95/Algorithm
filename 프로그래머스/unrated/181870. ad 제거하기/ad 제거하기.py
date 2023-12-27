def solution(strArr):
    answer = []
    for string in strArr:
        if not "ad" in string:
            answer.append(string)
    return answer