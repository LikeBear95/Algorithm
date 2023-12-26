def solution(my_string):
    answer = ''
    for string in my_string:
        if not string in answer:
            answer += string
    return answer