def solution(food):
    tmp = ''
    for i, s in enumerate(food):
        tmp += str(i) * (s // 2)
    answer = tmp + '0' + tmp[::-1]
    return answer