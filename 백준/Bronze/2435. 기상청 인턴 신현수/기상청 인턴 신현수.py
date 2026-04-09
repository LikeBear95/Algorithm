n, k = map(int, input().split())
l = list(map(int, input().split()))
t = []

for i in range(n-k+1):
    t.append(sum(l[i:i+k]))

print(max(t))