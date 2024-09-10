import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

sum_lst = [0] * (n+1)
for i in range(1, n+1):
    sum_lst[i] = sum_lst[i-1] + lst[i-1]

for i in range(int(input())):
    s, e = map(int, input().split())
    print(sum_lst[e] - sum_lst[s-1])
