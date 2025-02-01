l = []
for _ in range(10):
    l.append(int(input()))
s = set(l)
m = [0, 0]
for i in s:
    n = l.count(i)
    if m[1] < n:
        m = [i, n]

print(sum(l)//10)
print(m[0])