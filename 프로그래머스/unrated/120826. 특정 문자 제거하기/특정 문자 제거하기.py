def solution(my_string, letter):
    answer = ''
    for tmp in my_string:
        if tmp == letter:
            pass
        else:
            answer += tmp
    return answer