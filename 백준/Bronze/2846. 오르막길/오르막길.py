n = int(input())
p = list(map(int, input().split()))
l, h = p[0], 0

for i in range(1,n):
    if p[i] <= p[i-1]:
        l = p[i]
    h = max(h, p[i]-l)
    
print(h)