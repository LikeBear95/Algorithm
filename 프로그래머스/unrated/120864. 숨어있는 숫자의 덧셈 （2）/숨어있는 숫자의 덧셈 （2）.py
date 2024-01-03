def solution(my_string):
    answer = 0
    tmp = ''
    for string in my_string:
        if string.isdigit():
            tmp += string
        elif tmp:
            answer += int(tmp)
            tmp = ''
    if tmp:
        answer += int(tmp)
    return answer