def solution(arr):
    answer = []
    length = max(len(arr), len(arr[0]))
    for i in range(length):
        tmp = []
        for j in range(length):
            try:
                tmp.append(arr[i][j])
            except:
                tmp.append(0)
        answer.append(tmp)
    return answer