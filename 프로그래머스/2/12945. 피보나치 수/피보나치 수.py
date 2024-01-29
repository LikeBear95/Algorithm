def F(n):
    lst = [0, 1]
    for n in range(2, n+1):
        lst.append((lst[n-2] + lst[n-1]) % 1234567)
    return lst[-1]
    
def solution(n):
    answer = F(n) 
    return answer