n, m = map(int, input().split())
ball = [0] * n
for i in range(m):
    s, e, b = map(int, input().split())
    for j in range(s-1, e):
        ball[j] = b
print(*ball)