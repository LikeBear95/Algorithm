import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()
print("YES" if 'gori' in s else "NO")