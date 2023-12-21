def solution(emergency):
    answer = []
    sorted_emergency = sorted(emergency, reverse=True)
    for tmp in emergency:
        for j, num in enumerate(sorted_emergency):
            if tmp == num:
                answer.append(j + 1)
                break
    return answer