import sys
input = sys.stdin.readline

l = [1, 0, 0]

for i in input().rstrip():
    if i == "A":
        l[0], l[1] = l[1], l[0]
    elif i == "B":
        l[1], l[2] = l[2], l[1]
    elif i == "C":
        l[0], l[2] = l[2], l[0]

print(l.index(1)+1)