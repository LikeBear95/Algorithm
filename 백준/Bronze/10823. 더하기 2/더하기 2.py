import sys
input = sys.stdin.readline

s = ""
while True:
    t = input().rstrip()
    if t:
        s = s+t
    else:
        break

print(sum(list(map(int, s.split(",")))))