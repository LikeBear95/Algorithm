import sys
input = sys.stdin.readline

n = int(input())-1
m = 0
for _ in range(int(input())):
    t, z = map(str, input().split())
    m += int(t)
    if m > 210:
        break
    else:
        if z == "T":
            n += 1

print(n%8+1)