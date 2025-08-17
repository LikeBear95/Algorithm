import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    print(s, "is", end=" ")
    if s.count("g")+s.count("G") > s.count("b")+s.count("B"):
        print("GOOD")
    elif s.count("g")+s.count("G") < s.count("b")+s.count("B"):
        print("A BADDY")
    else:
        print("NEUTRAL")