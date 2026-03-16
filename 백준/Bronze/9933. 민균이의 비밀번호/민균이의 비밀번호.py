import sys
input = sys.stdin.readline

l = []

for _ in range(int(input())):
    s = input().rstrip()
    l.append(s)
    if s[::-1] in l:
        print(len(s), s[len(s)//2])
        break