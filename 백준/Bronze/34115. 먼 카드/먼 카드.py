n = int(input())
l = list(map(int, input().split()))
p = [[] for _ in range(n)]
m = 0

for i in range(2*n):
    p[l[i]-1].append(i)

for t in p:
    m = max(m, t[1]-t[0]-1)

print(m)