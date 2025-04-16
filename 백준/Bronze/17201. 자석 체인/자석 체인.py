import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()

print("No" if '11' in s or '22' in s else "Yes")
