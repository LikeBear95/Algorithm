import sys
input = sys.stdin.readline

def fib(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fib(num-1) + fib(num-2)

def fibonacci(num):
    lst = [0] * (num+1)
    lst[1], lst[2] = 1, 1
    cnt = 0
    for i in range(3, num+1):
        cnt += 1
        lst[i] = lst[i-1] + lst[i-2]
    return [lst, cnt]

n = int(input())
print(fibonacci(n)[0][n], fibonacci(n)[1])
