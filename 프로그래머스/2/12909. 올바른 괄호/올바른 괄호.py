def solution(s):
    tmp = [0, 0]
    if s.count('(') != s.count(')'):
        return False
    for i in s:
        if i == '(':
            tmp[0] += 1
        else:
            tmp[1] += 1
            if tmp[0] < tmp[1]:
                return False
    return True
            