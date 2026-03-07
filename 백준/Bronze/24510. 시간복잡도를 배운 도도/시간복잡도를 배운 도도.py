import sys
input = sys.stdin.readline

x = 0
for _ in range(int(input())):
    s = input().rstrip()
    x = max(x, s.count('for')+s.count('while'))

print(x)