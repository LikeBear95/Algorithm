def solution(sides):
    answer = len([num for num in range(max(sides) - min(sides) + 1, sum(sides))])
    return answer