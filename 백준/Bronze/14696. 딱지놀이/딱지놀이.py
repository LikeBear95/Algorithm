import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a = [0,0,0,0,0]
    b = [0,0,0,0,0]

    al = list(map(int, input().split()))
    bl = list(map(int, input().split()))

    for i in al[1:]:
        a[i] += 1
    for j in bl[1:]:
        b[j] += 1

    for k in range(4,0,-1):
        if a[k] > b[k]:
            print("A")
            break
        elif a[k] < b[k]:
            print("B")
            break
    else:
        print("D")