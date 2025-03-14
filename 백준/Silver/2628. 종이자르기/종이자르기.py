x, y = map(int, input().split())
row = [0] * x
col = [0] * y

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a:
        row[b] = 1
    else:
        col[b] = 1

rl, cl = [], []
rt, ct = 1, 1
for i in range(1, x):
    if row[i]:
        rl.append(rt)
        rt = 1
    else:
        rt += 1
rl.append(rt)

for j in range(1, y):
    if col[j]:
        cl.append(ct)
        ct = 1
    else:
        ct += 1
cl.append(ct)

print(max(rl)*max(cl))