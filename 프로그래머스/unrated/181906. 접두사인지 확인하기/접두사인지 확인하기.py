def solution(my_string, is_prefix):
    answer = 0
    if len(my_string) < len(is_prefix):
        return answer
    
    for i in range(len(is_prefix)):
        if my_string[i] == is_prefix[i]:
            pass
        else:
            return answer
    else:
        answer = 1
    return answer