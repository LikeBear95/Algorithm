def solution(myString, pat):
    answer = 0
    tmp = ''
    for string in myString:
        if string == 'A':
            tmp += 'b'
        elif  string == 'B':
            tmp += 'a'
    if pat in tmp.upper():
        answer = 1
    return answer