a, b = map(int, input().split())
l = [0]
n = 1
while True:
    if len(l) < b+1:
        l += [n]*n
        n += 1
    else:
        break

print(sum(l[a:b+1]))