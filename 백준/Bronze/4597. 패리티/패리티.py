import sys
input = sys.stdin.readline

while True:
    t = input().rstrip()
    if t == "#":
        break
        
    n = t.count("1")
    if n%2:
        if t[-1] == "o":
            print(t[:-1]+"0")
        else:
            print(t[:-1]+"1")
    else:
        if t[-1] == "o":
            print(t[:-1]+"1")
        else:
            print(t[:-1]+"0")