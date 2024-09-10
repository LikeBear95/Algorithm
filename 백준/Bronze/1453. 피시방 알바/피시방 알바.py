import sys
input = sys.stdin.readline

print(int(input()) - len(set(map(int, input().split()))))