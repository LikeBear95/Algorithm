def solution(myString):
    answer = ''
    for string in myString:
        if string in 'abcdefghijk':
            answer += 'l'
        else:
            answer += string
    return answer