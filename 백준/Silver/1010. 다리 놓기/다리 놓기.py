import sys
input = sys.stdin.readline

def factorial(num):
    tmp = 1
    if num > 1:
        for i in range(2, num+1):
            tmp *= i
    return tmp

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(factorial(m)//factorial(m-n)//factorial(n))
