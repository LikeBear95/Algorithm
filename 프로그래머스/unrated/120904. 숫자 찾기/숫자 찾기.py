def solution(num, k):
    answer = -1
    for number in str(num):
        if number == str(k):
            answer = str(num).index(number) + 1
            break
    return answer