import sys
input = sys.stdin.readline

def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n

n, k = map(int, input().split())
print(factorial(n) // (factorial(n-k) * factorial(k)))
