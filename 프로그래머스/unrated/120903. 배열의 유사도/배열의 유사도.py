def solution(s1, s2):
    answer = 0
    for string in s1:
        if string in s2:
            answer += 1
    return answer