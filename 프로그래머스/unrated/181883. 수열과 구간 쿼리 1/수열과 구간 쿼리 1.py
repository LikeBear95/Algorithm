def solution(arr, queries):
    answer = arr
    for query in queries:
        s, e = query
        for i in range(s, e+1):
            arr[i] += 1
    return answer