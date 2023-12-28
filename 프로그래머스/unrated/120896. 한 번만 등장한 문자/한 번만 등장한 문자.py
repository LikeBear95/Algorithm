def solution(s):
    answer = ''
    for string in 'abcdefghijklmnopqrstuvwxyz':
        if s.count(string) == 1:
            answer += string
    return answer