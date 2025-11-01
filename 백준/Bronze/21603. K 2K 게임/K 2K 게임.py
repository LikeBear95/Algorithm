def f(x):
    return x%10

n, k = map(int, input().split())
l = [x for x in range(1, n+1)]

for i in range(f(k), n+1, 10):
    l.remove(i)

for i in range(f(2*k), n+1, 10):
    l.remove(i)

print(len(l))
print(*l if l else "")