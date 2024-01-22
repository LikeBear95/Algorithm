def solution(brown, yellow):
    for i in range(3, brown + yellow):
        for j in range(3, i+1):
            if i*j == (brown + yellow) and (i-2)*(j-2) == yellow:
                return [i, j]
    return answer