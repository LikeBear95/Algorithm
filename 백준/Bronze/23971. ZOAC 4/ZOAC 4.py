h, w, n, m = map(int, input().split())
h = h//(n+1) + (1 if h%(n+1) else 0)
w = w//(m+1) + (1 if w%(m+1) else 0)
print(h*w)