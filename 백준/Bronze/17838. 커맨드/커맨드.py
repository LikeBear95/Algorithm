import sys
input = sys.stdin.readline

for _ in range(int(input())):
    t = input().rstrip()
    f = 0
    for i in range(len(t)-6):
        s = t[i:i+7]
        if (
            len(t) == 7 and
            len(set(t)) == 2 and
            t[0] == t[1] == t[4] and
            t[2] == t[3] == t[5] == t[6]
        ):
            f = 1
            break
    print(f)
