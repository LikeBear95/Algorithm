import sys
input = sys.stdin.readline

def kantor(s, e, c):
    if s == e:
        return c
    else:
        c = c + " " * len(c) + c
        return kantor(s+1, e, c)

def inputNum(n):
    return kantor(0, n, "-")

while True:
    try:
        print(inputNum(int(input())))
    except:
        break
