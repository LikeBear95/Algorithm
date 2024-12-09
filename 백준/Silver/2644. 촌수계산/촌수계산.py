n = int(input())
l = [[] for _ in range(n+1)]
a, b = map(int, input().split())
for _ in range(int(input())):
    x, y = map(int, input().split())
    l[y].append(x)

al, bl = [a], [b]

while True:
    if l[a]:
        al.append(l[a][0])
        a = l[a][0]
    else:
        break

while True:
    if l[b]:
        bl.append(l[b][0])
        b = l[b][0]
    else:
        break

for i in al:
    if i in bl:
        print(len(al[:al.index(i)]) + len(bl[:bl.index(i)]))
        break
else:
    print(-1)