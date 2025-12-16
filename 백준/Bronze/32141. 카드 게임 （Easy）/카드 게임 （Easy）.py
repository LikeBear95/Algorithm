n, h = map(int, input().split())
l = list(map(int, input().split()))
m = 0

for i in range(n):
    m += l[i]
    if m >= h:
        print(i+1)
        break
else:
    print(-1)