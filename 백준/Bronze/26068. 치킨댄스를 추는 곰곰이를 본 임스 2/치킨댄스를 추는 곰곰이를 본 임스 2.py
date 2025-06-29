import sys
input = sys.stdin.readline

n = int(input())
c = 0
for _ in range(n):
    s = int(input().rstrip()[2:])
    c += 1 if s <= 90 else 0

print(c)