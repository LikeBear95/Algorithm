T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dist = abs(len(A) - len(B))
    answer = 0

    if len(A) > len(B):
        for i in range(len(A) - len(B) + 1):
            cnt = 0
            for j in range(len(B)):
                cnt += A[i + j] * B[j]
            if answer < cnt:
                answer = cnt

    else:
        for i in range(len(B) - len(A) + 1):
            cnt = 0
            for j in range(len(A)):
                cnt += B[i + j] * A[j]
            if answer < cnt:
                answer = cnt

    print(f'#{t} {answer}')
    