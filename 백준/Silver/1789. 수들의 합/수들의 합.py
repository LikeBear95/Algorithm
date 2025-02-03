n = int(input())
x, y = 0, 1
while x+y <= n:
    x += y
    y += 1
print(y-1)
