def solution(n):
    answer = []
    for num in range(n+1):
        if num % 2:
            answer.append(num)
        
    return answer