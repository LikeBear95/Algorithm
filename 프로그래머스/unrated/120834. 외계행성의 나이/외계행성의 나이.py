def solution(age):
    answer = ''
    num_to_alpha = { 0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e',
                   5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j'}
    for num in str(age):
        answer += num_to_alpha.get(int(num))
    return answer