def solution(arr, k):
    answer = []
    if k % 2:
        for num in arr:
            answer.append(num * k)
    else:
        for num in arr:
            answer.append(num + k)
    return answer