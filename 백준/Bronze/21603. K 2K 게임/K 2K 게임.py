def f(x):
    return x%10

n, k = map(int, input().split())
l = [x for x in range(1, n+1) if f(x)!=f(k) and f(x)!=f(2*k)]

print(len(l))
print(*l if l else "")