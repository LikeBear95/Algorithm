import sys
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    l.append(input().rstrip())
k = int(input())

if k == 1:
    for i in l:
        print(i)
elif k == 2:
    for i in l:
        print(i[::-1])
else:
    for i in l[::-1]:
        print(i)