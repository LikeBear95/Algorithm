import sys
input = sys.stdin.readline

s = "CAMBRIDGE"
x = ""
t = input().rstrip()

for i in t:
    if i not in s:
        x += i

print(x)