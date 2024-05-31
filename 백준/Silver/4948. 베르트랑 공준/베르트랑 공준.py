import math

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    return is_prime

while True:
    n = int(input())
    if n == 0:
        break

    limit = 2 * n
    is_prime = sieve_of_eratosthenes(limit)
    
    prime_count = 0
    for i in range(n + 1, 2 * n + 1):
        if is_prime[i]:
            prime_count += 1

    print(prime_count)
