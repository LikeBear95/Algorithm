import sys
input = sys.stdin.readline

for _ in range(int(input())):
    t = input().rstrip()
    if len(t) >= 10 and t[:10] == "Simon says":
        print(t[10:])