def f(i, N, s, K):
    global cnt
    if i == N:
        if s ==K:
            cnt += 1
    else:
        f(i+1, N, s+arr[i], K)
        f(i, N, s, K)

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    for i in range( 1<< N):
        s = 0
        for j in range(N):
            if i&(1<<j):
                s += arr[j]
        if s == K:
            cnt += 1
            
    print(f'#{tc} {cnt}')
    