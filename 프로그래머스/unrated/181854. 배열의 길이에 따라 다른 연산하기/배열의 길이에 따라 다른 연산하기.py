def solution(arr, n):
    answer = []
    for index in range(len(arr)):
        answer.append(arr[index] + (len(arr)+index) % 2 * n)
    return answer