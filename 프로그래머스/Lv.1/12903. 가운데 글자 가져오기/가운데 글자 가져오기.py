def solution(s):
    answer = s[len(s)//2]
    if not len(s) % 2:
        answer = s[len(s)//2-1] + answer
    return answer