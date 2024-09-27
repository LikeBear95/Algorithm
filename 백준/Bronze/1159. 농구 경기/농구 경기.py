import sys
input = sys.stdin.readline

d = {}
for _ in range(int(input())):
    s = input().rstrip()
    if s[0] in d:
        d[s[0]] += 1
    else:
        d[s[0]] = 1

l = []
for i in sorted(d):
    if d.get(i) >= 5:
        l.append(i)

if l:
    print("".join(l))
else:
    print("PREDAJA")