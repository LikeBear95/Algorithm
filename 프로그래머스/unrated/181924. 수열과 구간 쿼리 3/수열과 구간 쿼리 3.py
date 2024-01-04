def solution(arr, queries):
    answer = arr
    for query in queries:
        i, j = query
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
    return answer