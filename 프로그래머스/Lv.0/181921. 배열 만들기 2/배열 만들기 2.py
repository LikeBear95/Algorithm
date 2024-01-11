def solution(l, r):
    answer = []
    key = '12346789'
    for num in range(l, r+1):
        for n in str(num):
            if n in key:
                break
        else:
            answer.append(num)
    if not answer:
        answer.append(-1)
    return answer