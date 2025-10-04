import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == "#":
        break

    n = 0
    for i in s:
        if i in ["a","e","i","o","u"]:
            n = s.index(i)
            break
    print(s[n:]+s[:n]+"ay")