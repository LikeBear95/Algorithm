def solution(k, m, score):
    answer = 0
    for p in sorted(score)[len(score)%m::m]:
        answer += p * m
    return answer