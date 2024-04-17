n, m = map(int, input().split())
lst = list(map(int, input().split()))
answer = 0
for a in range(n-2):
    for b in range(a+1,n-1):
        for c in range(b+1,n):
            sum = lst[a] + lst[b] + lst[c]
            if sum <= m and sum > answer:
                answer = sum

print(answer)