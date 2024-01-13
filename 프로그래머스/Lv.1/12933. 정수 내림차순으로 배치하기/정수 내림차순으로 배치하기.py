def solution(n):
    answer = ''.join(sorted([x for x in str(n)], reverse=True))
    return int(answer)