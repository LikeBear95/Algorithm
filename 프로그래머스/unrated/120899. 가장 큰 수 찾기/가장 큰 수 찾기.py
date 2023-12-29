def solution(array):
    answer = []
    answer.append(sorted(array)[-1])
    answer.append(array.index(answer[0]))
    return answer