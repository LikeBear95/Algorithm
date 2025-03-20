import sys
input = sys.stdin.readline

for _ in range(int(input())):
    h, w, n = map(int, input().split())
    floor = h if n%h == 0 else n%h
    room = (n-1) // h+1
    print(f'{floor}{room:02d}')