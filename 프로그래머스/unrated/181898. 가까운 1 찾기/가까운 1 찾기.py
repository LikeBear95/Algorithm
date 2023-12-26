def solution(arr, idx):
    answer = -1
    for i, num in enumerate(arr):
        if idx > i:
            continue
        if num:
            answer = i
            break
    return answer