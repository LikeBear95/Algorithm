import sys
input = sys.stdin.readline

while True:
    l = list(map(int, input().split()))
    if l == [0]:
        break
    t = 0
    for i in l[1:]:
        if i == t:
            pass
        else:
            t = i
            print(i, end=" ")
    print("$")