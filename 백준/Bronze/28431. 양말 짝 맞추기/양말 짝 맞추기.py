l = []
for _ in range(5):
    n = int(input())
    if n in l:
        l.remove(n)
    else:
        l.append(n)

print(*l)