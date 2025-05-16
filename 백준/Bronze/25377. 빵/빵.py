t = -1
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a <= b:
        t = b if t==-1 else min(t,b)

print(t)