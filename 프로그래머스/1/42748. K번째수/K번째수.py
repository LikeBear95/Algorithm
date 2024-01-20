def solution(array, commands):
    answer = []
    for lst in commands:
        i, j, k = lst
        answer.append(sorted(array[i-1:j])[k-1])
    return answer