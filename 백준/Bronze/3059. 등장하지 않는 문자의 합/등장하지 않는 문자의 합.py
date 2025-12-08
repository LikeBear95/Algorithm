import sys
input = sys.stdin.readline

n = 2015

for _ in range(int(input())):
    s = set(input().rstrip())
    print(n - sum(ord(c) for c in s))
