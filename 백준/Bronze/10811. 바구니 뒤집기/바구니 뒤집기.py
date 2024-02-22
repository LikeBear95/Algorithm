n, m = map(int, input().split())
lst = [x+1 for x in range(n)]
for i in range(m):
    s, e = map(int, input().split())
    lst[s-1:e] = lst[s-1:e][::-1]
print(*lst)