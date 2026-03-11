import sys
input = sys.stdin.readline

x, y = map(int, input().split())
m = x*1000/y

for _ in range(int(input())):
    x, y = map(int, input().split())
    m = min(m, x*1000/y)

print(round(m, 2))