import sys
input = sys.stdin.readline

t = 0
for _ in range(int(input())):
    s = input().rstrip()
    if s[0] == "C":
        t += 1

print(t)