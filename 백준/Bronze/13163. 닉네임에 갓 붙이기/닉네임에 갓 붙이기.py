import sys
input = sys.stdin.readline

for _ in range(int(input())):
    l = list(map(str, input().rstrip().split()))
    print('god'+''.join(l[1:]))
