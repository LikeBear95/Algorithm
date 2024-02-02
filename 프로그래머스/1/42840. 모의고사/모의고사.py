def solution(answers):
    answer = []
    tmp = [0,0,0]
    two = [1,3,4,5]
    three = [3,1,2,4,5]
    for i, n in enumerate(answers):
        if n == i % 5 + 1:
            tmp[0] += 1
        if i % 2 == 0 and n == 2:
            tmp[1] += 1
        elif i % 2 and two[(i % 8) // 2] == n:
            tmp[1] += 1
        if n == three[(i % 10) // 2]:
            tmp[2] += 1
    for i, num in enumerate(tmp):
        if num == max(tmp):
            answer.append(i+1)
    return answer