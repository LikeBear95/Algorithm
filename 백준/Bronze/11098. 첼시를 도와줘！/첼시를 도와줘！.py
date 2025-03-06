import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, s = 0, ''
    for _ in range(int(input())):
        a, b = map(str, input().split())
        if n < int(a):
            n = int(a)
            s = b

    print(s)