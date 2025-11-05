import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == "#":
        break
    print(f'{s[0]} {s.lower().count(s[0])-1}')
    