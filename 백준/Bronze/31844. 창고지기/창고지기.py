import sys
input = sys.stdin.readline

s = input().rstrip()
r = s.index('@')
b = s.index('#')
g = s.index('!')

print(abs(r-g)-1 if r < b < g or g < b < r else -1)