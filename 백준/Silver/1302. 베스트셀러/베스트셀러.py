import sys
input = sys.stdin.readline

d = {}
for _ in range(int(input())):
    s = input().rstrip()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

print(sorted(d.items(), key=lambda x: (-x[1], x[0]))[0][0])