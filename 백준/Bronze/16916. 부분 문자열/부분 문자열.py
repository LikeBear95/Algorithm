import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

print(1 if t in s else 0)