import sys
input = sys.stdin.readline

d = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for _ in range(int(input())):
    x, y = map(int, input().split())
    print("Yes" if 0<=x<=23 and 0<=y<=59 else "No", end=" ")
    print("Yes" if 1<=x<=12 and 1<=y<=d[x] else "No")