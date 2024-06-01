# 다른사람꺼

import sys

prime = []
check = [0] * 1000001
check[0] = 1
check[1] = 1

for i in range(2, 1000001):
    if check[i] == 0:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            check[j] = 1

T = int(sys.stdin.readline())

for _ in range(T):
    count = 0
    N = int(sys.stdin.readline())
    for i in prime:
        if i >= N:
            break
        if not check[N - i] and i <= N-i:  # 순서만 다른거 counting 하지 않기 위해
            count += 1
    print(count)

/*
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    return is_prime

is_prime = sieve_of_eratosthenes(1000000)

for _ in range(int(input())):
    n = int(input())
    cnt = 0

    for i in range(2, n // 2 + 1):
        if is_prime[i] and is_prime[n - i]:
            cnt += 1

    print(cnt)
*/
