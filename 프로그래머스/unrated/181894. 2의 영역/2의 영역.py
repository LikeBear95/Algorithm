def solution(arr):
    tmp = [-1, -1]
    for i, num in enumerate(arr):
        if num == 2:
            if tmp[0] == -1:
                tmp[0] = i
            else:
                tmp[1] = i
    if tmp[0] == -1:
        answer = [-1]
    elif tmp[1] == -1:
        answer = [2]
    else:
        answer = arr[tmp[0]:tmp[1]+1]
    return answer