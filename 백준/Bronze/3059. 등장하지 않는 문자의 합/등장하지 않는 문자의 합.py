import sys
input = sys.stdin.readline

for _ in range(int(input())):
    t = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = input().rstrip()
    n = 2015

    for i in s:
        if i in t:
            t = t.replace(i, "")
            n -= ord(i)

    print(n)