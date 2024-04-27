lst = []
for _ in range(int(input())):
    tmp = list(map(int, input().split()))
    lst.append(tmp)
lst.sort()
for l in lst:
    print(*l)