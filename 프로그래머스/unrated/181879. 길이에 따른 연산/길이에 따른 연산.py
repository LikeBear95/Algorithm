def solution(num_list):
    answer = 0
    
    if len(num_list) >= 11:
        answer = sum(num_list)
    elif len(num_list) <= 10:
        tmp = 1
        for i in num_list:
            tmp *= i
        answer = tmp
    
    return answer