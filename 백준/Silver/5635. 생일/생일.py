import sys
input = sys.stdin.readline

l = []
for _ in range(int(input())):
    n, d, m, y = map(str, input().split())
    l.append([n, int(d), int(m), int(y)])

l = sorted(l, key = lambda x: (x[3], x[2], x[1]))
print(l[-1][0])
print(l[0][0])