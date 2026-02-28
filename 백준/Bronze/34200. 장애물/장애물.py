n = int(input())
l = [-1] + list(map(int, input().split()))
c = 0

for i in range(n):
    t = l[i+1] - l[i]
    if t == 1:
        print(-1)
        break
    else:
        c += t//2 + t%2
else:
    print(c)