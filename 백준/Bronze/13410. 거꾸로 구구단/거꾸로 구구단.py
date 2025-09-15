n, k = map(int, input().split())
l = [n*x for x in range(1,k+1)]
m = 0
for i in l:
    m = max(m, int(str(i)[::-1]))
print(m)