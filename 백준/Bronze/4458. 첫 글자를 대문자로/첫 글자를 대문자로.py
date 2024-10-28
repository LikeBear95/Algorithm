import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    if ord(s[0]) >= 97:
        print(f'{s[0].upper()+s[1:]}')
    else:
        print(s)