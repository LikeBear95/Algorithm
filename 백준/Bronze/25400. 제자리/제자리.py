import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

for i in range(1, n+1):
    if i in lst:
        lst = lst[lst.index(i):]
        n -= 1
    else:
        break

print(n)

