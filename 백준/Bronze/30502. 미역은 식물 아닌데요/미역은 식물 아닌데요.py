import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = [[-1,-1] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(str, input().split())
    if b == 'P':
        l[int(a)][0] = 1 if int(c) == 1 else 0
    elif b == 'M':
        l[int(a)][1] = 1 if int(c) == 1 else 0
        
print(l.count([1,0]), l.count([1,0])+l.count([-1,0])+l.count([1,-1])+l[1:].count([-1,-1]))