import sys
input = sys.stdin.readline

n, k = map(int, input().split())
l = list(map(int, input().split()))
print(sorted(l)[k-1])