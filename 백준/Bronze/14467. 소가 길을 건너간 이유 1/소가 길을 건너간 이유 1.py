n = int(input())
l = [-1]*11
x = 0

for _ in range(n):
    c, p = map(int, input().split())
    if l[c] == -1:
        l[c] = p
    else:
        if l[c] != p:
            x += 1
            l[c] = p

print(x)