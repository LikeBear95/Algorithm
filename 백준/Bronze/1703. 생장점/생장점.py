import sys
input = sys.stdin.readline

while True:
    l = list(map(int, input().split()))
    if l[0] == 0:
        break

    n = 1
    for i in range(1,l[0]*2,2):
        n = l[i]*n - l[i+1]
    print(n)
