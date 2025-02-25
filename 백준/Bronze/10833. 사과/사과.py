import sys
input = sys.stdin.readline

n = 0
for _ in range(int(input())):
    s, a = map(int, input().split())
    n += a%s

print(n)