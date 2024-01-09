def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query
        tmp = [x for x in arr[s:e+1] if x > k]
        if tmp:
            answer.append(min(tmp))
        else:
            answer.append(-1)
    return answer