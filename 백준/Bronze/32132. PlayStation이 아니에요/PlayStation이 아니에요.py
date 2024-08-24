import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()

while True:
    if "PS4" in s:
        s = s.replace("PS4", "PS")
    elif "PS5" in s:
        s = s.replace("PS5", "PS")
    else:
        break

print(s)
