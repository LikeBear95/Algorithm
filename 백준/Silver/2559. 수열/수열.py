import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temp = list(map(int, input().split()))
lst = [sum(temp[:k])]

for i in range(n-k):
    lst.append(lst[i] - temp[i] + temp[i+k])

print(max(lst))
