n = int(input())
lst = list(map(int, input().split()))
answer = []
for i in range(n):
    if lst[i] not in answer:
        answer.append(lst[i])
print(*sorted(answer))