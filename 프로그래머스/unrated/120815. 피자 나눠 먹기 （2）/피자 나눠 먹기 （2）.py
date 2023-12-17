import math

def solution(n):
    gcd = math.gcd(n, 6)
    answer = n // gcd
    return answer