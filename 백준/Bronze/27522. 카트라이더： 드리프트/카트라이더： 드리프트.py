import sys
input = sys.stdin.readline

l = []
s = [10, 8, 6, 5, 4, 3, 2, 1, 0]
r, b = 0, 0

for _ in range(8):
    time, team = map(str, input().rstrip().split())
    m, ss, sss = map(int, time.split(":"))
    l.append([m*60*1000+ss*1000+sss,team])

l = sorted(l)
for i in range(8):
    if l[i][1] == 'R':
        r += s[i]
    else:
        b += s[i]

print("Red" if r>b else "Blue")
    