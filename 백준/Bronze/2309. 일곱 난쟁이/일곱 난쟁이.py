import sys
input = sys.stdin.readline

def check():
    global lst
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == total:
                return [lst[i], lst[j]]

lst = [int(input()) for _ in range(9)]

lst.sort()
total = sum(lst) - 100

for i in check():
    lst.remove(i)

for i in lst:
    print(i)

