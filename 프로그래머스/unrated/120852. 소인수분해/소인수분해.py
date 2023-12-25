def solution(n):
    answer = []
    for num in range(2, n+1):
        if n % num == 0:
            for i in answer:
                if num % i == 0:
                    break
                else:
                    pass
            else:
                answer += [num]
            
    return answer