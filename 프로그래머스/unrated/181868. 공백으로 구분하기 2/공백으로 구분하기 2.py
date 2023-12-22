def solution(my_string):
    answer = list(map(str, my_string.split(' ')))
    while('' in answer):
        answer.remove('')
    return answer