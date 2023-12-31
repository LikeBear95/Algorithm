def solution(myString):
    answer = list(map(str, myString.split('x')))
    while("" in answer):
        answer.remove("")
    return sorted(answer)