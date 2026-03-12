n = int(input())
l = list(map(int, input().split()))
m = l.index(max(l))

for i in range(1, n):
    if i < m and l[i] <= l[i-1]:
        print("NO")
        break
    elif i > m and l[i] >= l[i-1]:
        print("NO")
        break
else:
    print("YES")