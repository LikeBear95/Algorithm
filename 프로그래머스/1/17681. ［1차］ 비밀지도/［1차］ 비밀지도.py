def solution(n, arr1, arr2):
    answer = []
    for num1, num2 in zip(arr1, arr2):
        tmp = ''
        for i in range(n):
            if num1 % 2 or num2 % 2:
                tmp += '#'
            else:
                tmp += ' '
            num1 //= 2
            num2 //= 2
        answer.append(tmp[:][::-1])
    return answer