import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    
    l = []
    for _ in range(n):
        l.append(input().rstrip())

    print(sorted(l, key=str.lower)[0])