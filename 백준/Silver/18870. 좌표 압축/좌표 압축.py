n = int(input())
lst = list(map(int, input().split()))

sl = sorted(list(set(lst)))
dic = {}

for i, v in enumerate(sl):
    dic[v] = i

for i in lst:
    print(dic[i], end = " ")