import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lstsum = [0]
tmp = 0

for i in range(n):
    tmp += lst[i]
    lstsum.append(tmp)

for _ in range(m):
    s, e = map(int, input().split())
    print(lstsum[e] - lstsum[s-1])
