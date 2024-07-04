import sys
input = sys.stdin.readline

def fibo(num, memo):
    if num in memo:
        return memo[num]

    if num == 0:
        memo[0] = (1, 0)
    elif num == 1:
        memo[1] = (0, 1)
    else:
        fibo0 = fibo(num-1, memo)
        fibo1 = fibo(num-2, memo)
        memo[num] = (fibo0[0] + fibo1[0], fibo0[1] + fibo1[1])

    return memo[num]

for _ in range(int(input())):
    result = fibo(int(input()), {})
    print(result[0], result[1])
