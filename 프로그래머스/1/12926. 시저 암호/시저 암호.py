def solution(s, n):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        elif i.islower():
            answer += alpha[(alpha.index(i) + n) % len(alpha)]
        else:
            answer += alpha[(alpha.index(i.lower()) + n) % len(alpha)].upper()
    return answer