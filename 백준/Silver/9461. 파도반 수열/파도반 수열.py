import sys
input = sys.stdin.readline

def P(num):
    if num <= 3:
        return 1
    lst = [0] * (num+1)
    lst[1], lst[2], lst[3] = 1, 1, 1
    for i in range(3, num+1):
        lst[i] = lst[i-2] + lst[i-3]
    return lst[-1]

for _ in range(int(input())):
    print(P(int(input())))
