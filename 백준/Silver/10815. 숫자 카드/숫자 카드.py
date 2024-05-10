n = int(input())
lst = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

dic = {}
for i in range(n):
    dic[lst[i]] = 0

for i in range(m):
    if check[i] in dic:
        print(1, end=' ')
    else:
        print(0, end=' ')