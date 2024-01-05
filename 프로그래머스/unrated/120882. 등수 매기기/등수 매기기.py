def solution(score):
    avg = [sum(x) / 2 for x in score]
    sorted_avg = sorted(avg, reverse = True)
    answer = [sorted_avg.index(x) + 1 for x in avg]
    return answer