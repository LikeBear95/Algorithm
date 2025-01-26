w = []
for i in range(10):
    w.append(int(input()))

k = []
for j in range(10):
    k.append(int(input()))

print(sum(sorted(w)[-3:]), sum(sorted(k)[-3:]))