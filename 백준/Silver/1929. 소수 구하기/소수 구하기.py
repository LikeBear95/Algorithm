def sieve_of_eratosthenes(start, limit):
    # 초기화: 모든 숫자를 소수로 가정
    is_prime = [True] * (limit + 1)
    p = 2

    while (p * p <= limit):
        # is_prime[p]가 여전히 True라면
        if is_prime[p]:
            # p의 배수를 모두 지워나감
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1

    # start가 2보다 작을 경우, 2부터 검사
    if start < 2:
        start = 2

    # True로 남아 있는 숫자들을 소수로 간주
    prime_numbers = [p for p in range(start, limit + 1) if is_prime[p]]
    return prime_numbers

# 사용자로부터 입력 받기
start, limit = map(int, input().split())
primes = sieve_of_eratosthenes(start, limit)
for prime in primes:
    print(prime)
