import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = [1]
for i in range(1, n+1):
    tmp = []
    for j in range(i):
        if j == 0 or j == i-1:
            tmp.append(1)
        else:
            tmp.append(lst[j-1]+lst[j])
    lst = tmp
    
print(lst[k-1])
