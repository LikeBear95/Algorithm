def solution(num_list):
    num_odd = ''
    num_even = ''
    for num in num_list:
        if num % 2:
            num_odd += str(num)
        else:
            num_even += str(num)
    answer = int(num_odd) + int(num_even)
    return answer