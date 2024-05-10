n = int(input())
check = list(map(int, input().split()))
m = int(input())
lst = list(map(int, input().split()))

dic = {}
for i in range(m):
    dic[lst[i]] = 0

for i in range(n):
    try:
        dic[check[i]] += 1
    except:
        pass

for i in range(m):
    print(dic[lst[i]], end=' ')