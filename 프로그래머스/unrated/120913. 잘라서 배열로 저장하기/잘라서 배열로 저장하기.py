def solution(my_str, n):
    answer = []
    tmp = 0
    for i in range(len(my_str)):
        if len(my_str[tmp:i]) == n:
            answer.append(my_str[tmp:i])
            tmp = i
    answer.append(my_str[tmp:])
    return answer