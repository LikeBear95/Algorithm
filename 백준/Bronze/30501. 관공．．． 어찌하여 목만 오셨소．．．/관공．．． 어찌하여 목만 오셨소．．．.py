import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    if "S" in s:
        print(s)
        break