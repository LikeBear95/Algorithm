def solution(arr, queries):
    answer = arr
    for query in queries:
        s, e, k = query
        for i in range(s, e+1):
            if not i % k:
                answer[i] += 1
    return answer