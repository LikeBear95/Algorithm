import sys
input = sys.stdin.readline

for i in range(int(input())):
    t = input().rstrip()
    n = int(input())
    m = 0
    for j in range(n):
        m += int(input())
    print("NO" if m%n else "YES")