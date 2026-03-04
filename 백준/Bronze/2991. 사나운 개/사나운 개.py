a, b, c, d = map(int, input().split())
p, m, n = map(int, input().split())

l = [0]*1000

for i in range(1000):
    if i%(a+b) < a:
        l[i] += 1
    if i%(c+d) < c:
        l[i] += 1

print(l[p-1])
print(l[m-1])
print(l[n-1])