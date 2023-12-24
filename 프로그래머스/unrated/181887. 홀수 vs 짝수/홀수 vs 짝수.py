def solution(num_list):
    tmp1 = 0
    tmp2 = 0
    for i, num in enumerate(num_list):
        if i % 2:
            tmp1 += num
        else:
            tmp2 += num
    answer = max(tmp1, tmp2)
    return answer