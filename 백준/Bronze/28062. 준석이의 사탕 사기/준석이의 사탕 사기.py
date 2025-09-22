n = int(input())
l = list(map(int, input().split()))

m = sum(l)

if m%2:
    t = min([x for x in l if x%2])
    print(m-t)
else:
    print(m)