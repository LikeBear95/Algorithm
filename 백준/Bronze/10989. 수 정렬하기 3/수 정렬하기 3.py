from sys import stdin

def input():
    return stdin.readline().rstrip()

n = int(input())
lst = [0] * 10001
for i in range(n):
    num = int(input())
    lst[num] = lst[num] + 1

for i in range(10001):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i)