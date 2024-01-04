def solution(arr, flag):
    answer = []
    for i, num in enumerate(arr):
        if flag[i]:
            answer += [num] * num * 2
        else:
            for _ in range(num):
                answer.pop()
    return answer