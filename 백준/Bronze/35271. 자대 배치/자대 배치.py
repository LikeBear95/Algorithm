import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = [0] + list(map(int, input().split()))

for _ in range(n):
    t = list(map(int, input().split()))
    for i in t:
        if l[i]:
            l[i] -= 1
            print(i, end=" ")
            break
    else:
        print(-1, end=" ")