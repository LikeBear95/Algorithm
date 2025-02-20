l = []
for _ in range(int(input())):
    s, n = map(str, input().split())
    l.append([s, int(n)])

print(sorted(l, key= lambda x:x[1])[0][0])