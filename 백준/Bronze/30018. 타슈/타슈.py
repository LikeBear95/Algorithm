n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = 0

for i in range(n):
    t = a[i]-b[i]
    m = m+t if t > 0 else m

print(m)