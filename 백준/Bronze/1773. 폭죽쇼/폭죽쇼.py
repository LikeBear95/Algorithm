import sys
input = sys.stdin.readline

n, c = map(int, input().split())
s = set()

for _ in range(n):
    t = int(input())
    if t in s:
        pass
    for i in range(t,c+1,t):
        s.add(i)

print(len(s))