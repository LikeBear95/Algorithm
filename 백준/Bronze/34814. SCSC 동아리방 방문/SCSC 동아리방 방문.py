n, m = map(int, input().split())
drink = list(map(int, input().split()))

for _ in range(m):
    l, h = map(int, input().split())
    if max(drink) == drink[h-1]:
        pass
    else:
        drink[l-1] -= 1

print(*drink)