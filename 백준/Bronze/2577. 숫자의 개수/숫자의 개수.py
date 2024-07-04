import sys
input = sys.stdin.readline

number = str(int(input()) * int(input()) * int(input()))
lst = [0] * 10
for i in number:
    lst[int(i)] += 1

for i in lst:
    print(i)
