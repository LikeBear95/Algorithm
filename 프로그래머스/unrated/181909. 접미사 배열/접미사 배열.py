def solution(my_string):
    answer = []
    for index in range(len(my_string)):
        answer.append(my_string[index:])
    answer.sort()
    return answer