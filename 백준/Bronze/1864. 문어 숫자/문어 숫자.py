import sys
input = sys.stdin.readline

d = {"-":0, "\\":1, "(":2, "@":3, "?":4, ">":5, "&":6, "%":7, "/":-1, }

while True:
    s = input().rstrip()
    if s == "#":
        break

    n = len(s)
    x = 0
    for i in range(n):
       x += d[s[i]] * 8**(n-i-1)
    print(x)