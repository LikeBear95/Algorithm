import sys
input = sys.stdin.readline

s = input().rstrip()
print("true" if s == s[::-1] else "false")