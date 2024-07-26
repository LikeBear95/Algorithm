import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

lst = sorted(lst)
answer = 0

for i in range(n):
    answer += lst[i] * (n-i)

print(answer)
