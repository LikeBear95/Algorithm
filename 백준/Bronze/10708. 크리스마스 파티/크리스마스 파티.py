n = int(input())
m = int(input())
t = list(map(int, input().split()))
s = [0 for _ in range(n)]

for i in range(m):
    e = list(map(int, input().split()))
    c = 0
    for j in range(n):
        if t[i] == e[j]:
            s[j] += 1
        else:
            c += 1

    s[t[i]-1] += c

for x in s:
    print(x)