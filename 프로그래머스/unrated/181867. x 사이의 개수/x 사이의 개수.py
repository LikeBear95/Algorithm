def solution(myString):
    answer = []
    cnt = 0
    for string in myString:
        if string == "x":
            answer.append(cnt)
            cnt = 0
        else:
            cnt += 1
    answer += [cnt]
    return answer