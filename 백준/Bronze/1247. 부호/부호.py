import sys
input = sys.stdin.readline

for _ in range(3):
    s = 0
    for i in range(int(input())):
        s += int(input())
    if s == 0:
        print(0)
    else:
        print("+" if s>0 else "-")