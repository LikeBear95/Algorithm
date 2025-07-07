n = int(input())
l = []
for _ in range(n):
    t = list(map(int, input().split()))
    s = sum(t)
    if s >= 512:
        l.append(s)

print(min(l) if l else -1)