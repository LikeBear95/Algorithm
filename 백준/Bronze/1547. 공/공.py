answer = 1
for _ in range(int(input())):
    n, m = map(int, input().split())
    if answer == n:
        answer = m
    elif answer == m:
        answer = n

print(answer)