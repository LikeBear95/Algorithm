x = []
y = []
for i in range(3):
        tmp = list(map(int, input().split()))
        if tmp[0] in x:
                x.remove(tmp[0])
        else:
                x.append(tmp[0])
        if tmp[1] in y:
                y.remove(tmp[1])
        else:
                y.append(tmp[1])
print(*x, *y)