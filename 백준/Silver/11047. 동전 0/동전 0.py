import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))

answer = 0
for i in range(n-1, -1, -1):
    answer += k // lst[i]
    k %= lst[i]
    if k == 0:
        break

print(answer)
