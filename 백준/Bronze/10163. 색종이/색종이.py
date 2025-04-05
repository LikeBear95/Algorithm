lst = [[0]*1001 for x in range(1001)]
n = int(input())
for i in range(1, n+1):
    x, y, w, h = map(int, input().split())
    for a in range(x, x+w):
        for b in range(y, y+h):
            lst[a][b] = i

for i in range(1, n+1):
    tmp = 0
    for j in lst:
        tmp += j.count(i)
    print(tmp)