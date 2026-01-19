import sys
input = sys.stdin.readline

for _ in range(int(input())):
    t = input().rstrip()
    if (
        len(t) == 7 and
        len(set(t)) == 2 and
        t[0] == t[1] == t[4] and
        t[2] == t[3] == t[5] == t[6]
    ):
        print(1)
    else:
        print(0)
