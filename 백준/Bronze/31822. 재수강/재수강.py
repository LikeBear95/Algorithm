import sys
input = sys.stdin.readline

s = input().rstrip()
c = 0
for _ in range(int(input())):
    t = input().rstrip()
    if s[:5] == t[:5]:
        c += 1

print(c)