n, m = map(int, input().split())
l = list(map(int, input().split()))
s, t = 0, 0

for i in l:
    s = 0 if s+i<0 else s+i
    t += 1 if s>=m else 0

print(t)