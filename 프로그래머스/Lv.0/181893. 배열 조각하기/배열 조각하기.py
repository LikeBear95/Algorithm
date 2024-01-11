def solution(arr, query):
    answer = arr
    for i in range(len(query)):
        if i % 2:
            answer = answer[query[i]:]
        else:
            answer = answer[:query[i]+1]
        # print(answer)
    return answer