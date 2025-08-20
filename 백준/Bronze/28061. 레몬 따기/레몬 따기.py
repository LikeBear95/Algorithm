n = int(input())
l = list(map(int, input().split()))

for i in range(n):
    l[i] = l[i]-n+i

print(max(l) if max(l) > 0 else 0)