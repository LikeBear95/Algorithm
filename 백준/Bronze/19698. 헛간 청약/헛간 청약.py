n, w, h, l = map(int, input().split())
t = (w//l)*(h//l)
print(t if t < n else n)