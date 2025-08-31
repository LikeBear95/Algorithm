import sys
input = sys.stdin.readline

n = int(input())
l = list(map(str, input().rstrip().split()))
s = l[0][0]

for i in l:
    if i != i[::-1] or i[0] != s or i[-1] != s:
        print(0)
        break
else:
    print(1)
