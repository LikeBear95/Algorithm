def solution(my_string):
    answer = []
    for string in my_string:
        if string.isdecimal():
            answer += [int(string)]
    answer.sort()
    return answer