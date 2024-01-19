def solution(s):
    answer = ''
    tmp = 0
    for i in s:
        if i.isalpha():
            if tmp % 2:
                answer += i.lower()
            else:
                answer += i.upper()
            tmp += 1
        else:
            answer += ' '
            tmp = 0
    return answer