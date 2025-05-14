import sys
input = sys.stdin.readline

n = int(input())
l1 = list(map(str, input().rstrip().split()))
l2 = list(map(str, input().rstrip().split()))

for i in l1:
    if not i in l2:
        print(i)
        break