n, k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort(key=lambda x:(-x[1],-x[2],-x[3]))

r = 1
tmp = lst[0][1:]
for i in range(n):
    c, g, s, b = lst[i]

    if tmp != [g, s, b]:
        r = i+1
        tmp = [g, s, b]

    if c == k:
        print(r)
        break
