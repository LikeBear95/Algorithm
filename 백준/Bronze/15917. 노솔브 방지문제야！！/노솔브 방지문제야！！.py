import sys
input = sys.stdin.readline

l = [2**x for x in range(32)]

for i in range(int(input())):
    print(1 if int(input()) in l else 0)
