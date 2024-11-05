import sys
input = sys.stdin.readline

lst = []
for i in range(int(input())):
    lst.append(int(input()))

m = 0
a = 0
for i in lst[::-1]:
    if i > m:
        a += 1
        m = i

print(a)