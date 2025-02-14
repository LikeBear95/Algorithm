import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    if len(s) >= 6 and len(s) <= 9:
        print("yes")
    else:
        print("no")