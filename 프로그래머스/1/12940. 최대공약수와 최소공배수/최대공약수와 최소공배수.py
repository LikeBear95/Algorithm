def solution(n, m):
    tmp = 1
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            tmp = i
    return [tmp, n * m / tmp]