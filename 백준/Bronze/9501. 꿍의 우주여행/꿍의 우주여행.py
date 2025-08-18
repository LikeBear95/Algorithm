import sys
input = sys.stdin.readline

for i in range(int(input())):
    n, d = map(int, input().split())
    t = 0
    for j in range(n):
        v, f, c = map(int, input().split())
        t += 1 if v*f/c >= d else 0
    print(t)