n, k = map(int, input().split())
f = [0 for _ in range(7)]
m = [0 for _ in range(7)]
r = 0

for _ in range(n):
    s, g = map(int, input().split())
    if s == 0:
        f[g] += 1
    else:
        m[g] += 1

for i in range(1,7):
    r += f[i]//k + (1 if f[i]%k else 0)
    r += m[i]//k + (1 if m[i]%k else 0)
    
print(r)