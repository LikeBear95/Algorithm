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
