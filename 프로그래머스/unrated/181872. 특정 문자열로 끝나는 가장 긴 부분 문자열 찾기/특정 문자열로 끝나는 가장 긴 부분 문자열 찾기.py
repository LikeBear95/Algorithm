def solution(myString, pat):
    answer = myString.replace(pat, '*')
    for i in range(len(answer)-1,-1,-1):
        if answer[i] == '*':
            answer = answer[:i+1]
            break
    answer = answer.replace('*', pat)
    return answer