import sys
input = sys.stdin.readline

n = int(input())
l = list(map(str, input().rstrip().split()))
s = input().rstrip()

print(l.count(s))