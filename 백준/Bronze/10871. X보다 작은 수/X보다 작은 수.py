n, x = map(int, input().split())
num = list(map(int, input().split()))
tmp = []
for i in range(n):
    if num[i] < x:
        tmp.append(num[i])
print(*tmp)