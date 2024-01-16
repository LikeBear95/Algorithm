def solution(s):
    answer = True
    if not(s.isdecimal() and (len(s) == 4 or len(s) == 6)):
        answer = False
    return answer