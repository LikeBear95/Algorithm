import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = input().rstrip()
print(0 if '0'*k in s else 1)