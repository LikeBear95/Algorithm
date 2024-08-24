import sys
input = sys.stdin.readline

lst = [0] * 117
lst[1] = 1
lst[2] = 1
lst[3] = 1
for i in range(4, 117):
    lst[i] = lst[i-1] + lst[i-3]
print(lst[int(input())])
