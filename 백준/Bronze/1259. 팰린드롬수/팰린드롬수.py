import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == "0":
        break
    elif s == s[::-1]:
        print("yes")
    else:
        print("no")
