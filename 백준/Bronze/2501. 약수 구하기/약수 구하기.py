p, q = map(int, input().split())
lst = []
for i in range(1, p+1):
        if p % i == 0:
                lst.append(i)

if len(lst) < q:
        print(0)
else:
        print(lst[q-1])