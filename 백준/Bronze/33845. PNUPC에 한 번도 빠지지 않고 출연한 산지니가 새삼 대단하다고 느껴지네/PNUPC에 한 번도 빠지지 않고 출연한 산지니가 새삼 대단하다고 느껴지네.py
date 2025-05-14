import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()
a = ''

for i in t:
    if not i in s:
        a += i

print(a)