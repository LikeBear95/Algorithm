n = int(input())
a = list(map(int, input().split()))
print(sum(a))
b = list(map(int, input().split()))
c = 0
for i in range(n):
    if not b[i]:
        c += a[i]
print(c)