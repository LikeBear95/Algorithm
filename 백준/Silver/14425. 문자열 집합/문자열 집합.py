n, m = map(int, input().split())
lst = []
answer = 0
for _ in range(n):
    lst.append(input())
for _ in range(m):
    tmp = input()
    if tmp in lst:
        answer += 1

print(answer)
