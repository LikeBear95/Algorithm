def solution(num_list, n):
    answer = [[]]
    for num in num_list:
        if len(answer[-1]) < n:
            answer[-1].append(num)
        else:
            answer.append([num])
    return answer