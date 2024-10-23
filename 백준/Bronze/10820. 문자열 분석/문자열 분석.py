import sys

while True:
    s = sys.stdin.readline().rstrip('\n')
    if not s:
        break
    l = [0, 0, 0, 0]
    for i in s:
        tmp = ord(i)
        if tmp == 32:
            l[3] += 1
        elif tmp >= 48 and tmp <= 57:
            l[2] += 1
        elif tmp >= 65 and tmp <= 90:
            l[1] += 1
        elif tmp >= 97 and tmp <= 122:
            l[0] += 1
            
    print(*l)