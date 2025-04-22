n, p = map(int, input().split())
l = [n]

while True:
    t = l[-1] * n
    t %= p
    if t in l:
        print(len(l[l.index(t):]))
        break
    else:
        l.append(t)