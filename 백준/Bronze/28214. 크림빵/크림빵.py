n, k, p = map(int, input().split())
lst = list(map(int, input().split()))
t = 0

for i in range(n):
    t += 1 if lst[k*i:k*(i+1)].count(0) < p else 0

print(t)