import sys
input = sys.stdin.readline

n, m = map(int, input().split())

for i in range(n):
    l = list(map(int, input().split()))
    t = []
    
    for j in range(0,m):
        x = 2126*l[3*j] + 7152*l[3*j+1] + 722*l[3*j+2]
        if x >= 2040000:
            t.append(".")
        elif x >= 1530000:
            t.append("-")
        elif x >= 1020000:
            t.append("+")
        elif x >= 510000:
            t.append("o")
        else:
            t.append("#")
    print("".join(t))