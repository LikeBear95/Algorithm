lst = [x for x in range(21)]

for _ in range(10):
    a, b = map(int, input().split())
    r = lst[a:b+1]
    r.reverse()
    lst = lst[:a] + r + lst[b+1:]

print(*lst[1:])