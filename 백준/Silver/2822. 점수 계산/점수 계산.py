l = [int(input()) for _ in range(8)]
n = sorted(l)[3:]
print(sum(n))
print(*sorted([l.index(x)+1 for x in n]))