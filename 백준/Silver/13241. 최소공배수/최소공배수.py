import math

# 최소공배수 구하는 함수 정의
def lcm(a, b):
    # gcd : 최대공약수
    return abs(a * b) // math.gcd(a, b)

# 입력 받기
a, b = map(int, input().split())

# 최소공배수 계산 및 출력
print(lcm(a, b))
