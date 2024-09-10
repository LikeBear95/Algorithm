import sys
input = sys.stdin.readline

s = input().rstrip()
f = sum([int(x) for x in s[:len(s)//2]])
b = sum([int(x) for x in s[len(s)//2:]])

print("LUCKY" if f == b else "READY")
