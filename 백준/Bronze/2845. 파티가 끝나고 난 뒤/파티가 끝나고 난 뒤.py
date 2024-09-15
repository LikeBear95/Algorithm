import sys
input = sys.stdin.readline

l, p = map(int, input().split())
lst = list(map(int, input().split()))
print(*[x-(l*p) for x in lst])