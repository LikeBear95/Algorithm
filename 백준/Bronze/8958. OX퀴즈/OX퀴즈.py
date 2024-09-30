import sys
input = sys.stdin.readline

for _ in range(int(input())):
    point = 0
    tmp = 0
    
    for i in input().rstrip():
        if i == "O":
            tmp += 1
            point += tmp
        else:
            tmp = 0

    print(point)