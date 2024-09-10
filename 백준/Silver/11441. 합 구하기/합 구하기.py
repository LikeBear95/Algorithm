import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

for i in range(int(input())):
    s, e = map(int, input().split())
    print(sum(lst[s-1:e]))
