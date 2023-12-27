def solution(myString):
    answer = ''
    for string in myString:
        if string == 'a' or string == 'A':
            answer += 'A'
        else:
            answer += string.lower()
    return answer