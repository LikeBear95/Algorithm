def solution(n):
    answer = 0
    # tmp = []
    while(n):
        answer += 1
        if answer % 3 == 0 or "3" in str(answer):
            # tmp.append(answer)
            pass
        else:
            n -= 1
    return answer