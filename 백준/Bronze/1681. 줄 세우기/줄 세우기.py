n, l = map(int, input().split())
c, t = 0, 0

while True:
    if c == n:
        print(t)
        break
    t += 1
    if str(l) not in str(t):
        c += 1