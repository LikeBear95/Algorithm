i = 0
pi = 3.1415927
while True:
    i += 1
    r, c, s = map(float, input().split())
    if c == 0:
        break
    r = r/5280/12
    d = pi*r*c
    h = s/60/60
    print(f"Trip #{i}: {d:.2f} {d/h:.2f}")