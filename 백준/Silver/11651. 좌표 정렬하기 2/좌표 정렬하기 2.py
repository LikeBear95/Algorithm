lst = []
for _ in range(int(input())):
    tmp = list(map(int, input().split()))
    lst.append(tmp)
lst.sort(key = lambda x:(x[1], x[0]))
for l in lst:
    print(*l)