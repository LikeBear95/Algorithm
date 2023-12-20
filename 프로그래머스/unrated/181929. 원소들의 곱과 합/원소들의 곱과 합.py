def solution(num_list):
    total = 0
    multi = 1
    for num in num_list:
        total += num
        multi *= num
    if multi < total ** 2:
        answer = 1
    else:
        answer = 0
    return answer