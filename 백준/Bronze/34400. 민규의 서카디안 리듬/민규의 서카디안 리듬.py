import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    print("ONLINE" if n%25 < 17 else "OFFLINE")