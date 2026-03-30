import sys
input = sys.stdin.readline

n, m = map(int, input().split())

for i in range(n):
    l = list(map(int, input().split()))
    for j in range(0,m):
        t = 2126*l[3*j] + 7152*l[3*j+1] + 722*l[3*j+2]
        if t >= 2040000:
            print(".", end="")
        elif t >= 1530000:
            print("-", end="")
        elif t >= 1020000:
            print("+", end="")
        elif t >= 510000:
            print("o", end="")
        else:
            print("#", end="")
    print()