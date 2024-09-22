import sys
input = sys.stdin.readline
ext = {}

for _ in range(int(input())):
    s = input().rstrip()
    tmp = s.index(".") + 1
    if s[tmp:] in ext:
        ext[s[tmp:]] += 1
    else:
        ext[s[tmp:]] = 1

for i in sorted(ext):
    print(i, ext[i])