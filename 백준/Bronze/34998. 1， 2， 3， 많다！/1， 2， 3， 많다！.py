import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = 0
    l = list(map(str, input().rstrip().split(" ")))
    for i in range(0,n*2+1,2):
        if l[i] == "!":
            print("!")
            break
        s += int(l[i])
    else:
        print(s if s<10 else "!")