import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))
c = 0

for _ in range(n-1):
    t = list(map(int, input().split()))
    s = 0
    for i in range(m):
        s += abs(l[i]-t[i])
    c += 1 if s > 2000 else 0

print("YES" if c>=(n-1)/2 else "NO")