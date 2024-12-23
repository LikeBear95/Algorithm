tc = 0
while True:
    tc += 1
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    print(f'Case {tc}: {l * (v//p) + min(l, v%p)}')